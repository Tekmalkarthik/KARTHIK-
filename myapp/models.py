
from django.db import models

class person(models.Model):
     FirstName=models.CharField( "FirstName",max_length=50,default=12)
     LastName=models.CharField( "LastName",max_length=50,default=12)
     Contact=models.IntegerField("Contact",default=12)
     Gender=models.CharField("gender",max_length=12,null='True')
     DOB=models.CharField("DOB",max_length=12,default=12)
     Address=models.CharField("Address",max_length=50,default=12)
     password=models.CharField("password",max_length=80,default=12)
     repassword=models.CharField("repassword",max_length=80,default=12)

