from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    

    ## Audit Info
    created_date = models.DateTimeField('date created')
    updated_date = models.DateTimeField('date updated')