from datetime import date, datetime
import string
from django.db import models
from django.db import models

# Create your models here.
class Message(models.Model):
   sender=models.CharField(max_length=100)
   receiver=models.CharField(max_length=100)
   message=models.CharField(max_length=1000)
   subject=models.CharField(max_length=200)
   date=models.DateTimeField(default=datetime.now,blank=True)
   is_read=models.BooleanField(default=False)
   
