from django.db import models
from django.contrib.auth.models import User
import uuid

class Ship(models.Model):
    ship_name  = models.CharField(max_length=50)
    ship_code = models.CharField(max_length=100, null=True, blank=True, unique=True, default=uuid.uuid4())
    
    ## M2M Fields
    users = models.ManyToManyField(User)
    
    ## Audit Info
    created_date = models.DateTimeField('date created')
    updated_date = models.DateTimeField('date updated')


class UserShip(models.Model):
    shipID = models.CharField(max_length=100)
    userID = models.CharField(max_length=100)
