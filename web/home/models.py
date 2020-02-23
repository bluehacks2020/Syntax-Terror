from django.db import models
from django.contrib.auth.models import User

def Post(models.models):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    email address = models.CharField(max_length= 30)
    address = models.CharField(max_length= 50)
    contact number = models.CharField(max_length= 13)
def __str__(self):
    return self.title

