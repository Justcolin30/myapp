from django.db import models


class Classname(models.Model):
    Name = models.CharField(max_length=50) 
    Location = models.Charfield(max_length=50)
    
class Persons(models.Model):
    
    