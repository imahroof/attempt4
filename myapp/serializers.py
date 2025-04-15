from rest_framework import serializers
from .models import Dashboard

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = ('User', 'Name', 'Organisation', 'Contact', 'Location', 'Notes', 'Date_Time', 'Widgets', 'Completed') 
        

