from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
import requests
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import DashboardSerializer
from rest_framework.decorators import api_view
from .models import Dashboard



@ensure_csrf_cookie
@require_http_methods(['GET'])
def set_csrf_token(request):
    """
    We set the CSRF cookie on the frontend.
    """
    return JsonResponse({'message': 'CSRF cookie set'})

@require_http_methods(['POST'])
def login_view(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        email = data['email']
        password = data['password']
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON'}, status=400)

    user = authenticate(request, username=email, password=password)
    if user:
        login(request, user)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'message': 'Invalid credentials'}, status=401)

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out'})

@require_http_methods(['GET'])
def user(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'username': request.user.username,
            'email': request.user.email
        })
    return JsonResponse({'message': 'Not logged in'})

@require_http_methods(['POST'])
def register(request):
    data = json.loads(request.body.decode('utf-8'))
    form = CreateUserForm(data)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': 'User registered successfully'}, status=201)
    else:
        errors = form.errors.as_json()
        return JsonResponse({'error': errors}, status=400)

# Fetch ransomware attacks (10 most recent attacks)
def fetch_ransomware_attacks(request):
    url = "https://www.ransomlook.io/api/recent/10"
    headers = {"User-Agent": "Mozilla/5.0"}  # stops requests being blocked by some APIs
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    return JsonResponse({"error": "Failed to fetch data"})

# Fetch 10 most recent CVE vulnerabilities
def fetch_cve_vulnerabilities(request):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    headers = {"User-Agent": "Mozilla/5.0"}  

    # fetch 10 most recent
    params = {
        "resultsPerPage": 10,
        "startIndex": 0
    }
    
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    return JsonResponse({"error": "Failed to fetch data"})

#GET all dashboards
@api_view(['GET'])
def getDashboards(request):

    if request.user.is_authenticated:
        # GET only the logged in users dashboards
        dashboards = Dashboard.objects.filter(User=request.user)  
        serializer = DashboardSerializer(dashboards, many=True)
        return Response(serializer.data)
    else:
        return Response({"error": "User not authenticated"})

#POST a new dashboard
@api_view(['POST'])
def postDashboard(request):
    if not request.user.is_authenticated:
        return Response({"error": "User not authenticated"})

    data = request.data.copy()
    data['User'] = request.user.id  # Set User from the authenticated request

    serializer = DashboardSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print("Serializer Errors:", serializer.errors)  # Debugging log
        return Response(serializer.errors)

# Delete a dashboard entry
@api_view(['DELETE'])
def deleteDashboard(request):
 
    if not request.user.is_authenticated:
        return Response({"error": "User not authenticated"})

    name = request.data.get('name')
    print(f"Received name: {name}")  # Debugging log
    print(f"Authenticated user: {request.user}")  # Debugging log

    try:
        # Find all dashboards with the given name for the authenticated user
        dashboards = Dashboard.objects.filter(Name=name, User=request.user)
        if not dashboards.exists():
            return Response({"error": "Dashboard not found or not authorized."})

        # Delete all matching dashboards
        dashboards.delete()
        return Response({"message": "Dashboard(s) deleted successfully."})
    except Exception as e:
        return Response({"error": "An error occurred while deleting the dashboard."})

# Add wigets to a dashboard entry
@api_view(['PUT'])
def addWidget(request):

    if not request.user.is_authenticated:
        return Response({"error": "User not authenticated"})

    name = request.data.get('name')  # get dashboard name to update widgets JSON array
    widgets = request.data.get('widgets')  # Get the updated widgets from the request body

    if not name or widgets is None:
        return Response({"error": "Name and widgets are required."})

    try:
        # Find dashboard by name, making sure it belongs to the user currently logged in
        dashboard = Dashboard.objects.get(Name=name, User=request.user)
        dashboard.Widgets = widgets  # Update the widgets field
        dashboard.save() 
        return Response({"message": "Dashboard updated successfully."})
    except Dashboard.DoesNotExist:
        return Response({"error": "Dashboard not found or not authorised."})
    except Exception as e:
        return Response(e)

# delete wigets in a dashboard entry, add but in reverse order
@api_view(['DELETE'])
def deleteWidget(request):

    if not request.user.is_authenticated:
        return Response({"error": "User not authenticated"})

    name = request.data.get('name')  
    widget_to_delete = request.data.get('widget')  

    if not name or widget_to_delete is None:
        return Response({"error": "Name and widget are required."})

    try:
        
        dashboard = Dashboard.objects.get(Name=name, User=request.user)

        widgets = dashboard.Widgets  
        if widget_to_delete not in widgets:
            return Response({"error": "Widget not found in the dashboard."})

        widgets.remove(widget_to_delete)
        dashboard.Widgets = widgets  
        dashboard.save() 

        return Response({"message": "Widget deleted successfully."})
    except Dashboard.DoesNotExist:
        return Response({"error": "Dashboard not found or not authorized."})
    except Exception as e:
        return Response(e)

# Completed status = boolean
@api_view(['PUT'])  # Allow PUT requests
def dashboardcomplete(request):

    if not request.user.is_authenticated:
        return Response({"error": "User not authenticated"})

    name = request.data.get('name') #get dashboard by name
    completed = request.data.get('completed') #get completed status 
    if not name or completed is None:
        return Response({"error": "Name and completed status are required."})
    try:
        dashboard = Dashboard.objects.get(Name=name, User=request.user)
        dashboard.Completed = completed  # Update the completed field
        dashboard.save()  # Save 
        return Response({"message": "Dashboard updated successfully."})
    except Dashboard.DoesNotExist:
        return Response({"error": "Dashboard not found or not authorized."})
    except Exception as e:
        print(f"Error updating dashboard: {e}")
        return Response(e)

    






 

