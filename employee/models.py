
from django.db import models

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.IntegerField()
    gender = models.CharField(max_length=100, default="", editable=True)
#   country = CountryField()
#  state = models.CharField(max_length=10, default="", editable=False)
    languages = models.CharField(max_length=10, default="", editable=True)
    eimage = models.ImageField()

    class Meta:
        db_table = "employee"
