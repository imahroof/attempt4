from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

class Dashboard(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE,)
    Name = models.CharField(max_length=255)
    Organisation = models.CharField(max_length=255)
    Contact = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    Notes = models.CharField(max_length=500, blank=True, null=True)  # Added Notes field
    Date_Time = models.DateTimeField()
    Widgets = models.JSONField(default=list) 
    Completed = models.BooleanField(default=False)  # Added completed field





    

    

    
