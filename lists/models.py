from django.db import models

class CV(models.Model):
    name_surname = models.TextField(default='');
    address = models.TextField(default='');
    email = models.EmailField(default='');
    about_description = models.TextField(default='');
    
class JOB(models.Model):
    job_title = models.TextField(default='');
    company = models.TextField(default='');
    job_description = models.TextField(default='');
    job_dates = models.TextField(default='');

#from django.db import models
#
#class Item(models.Model):
#    text = models.TextField(default='')
#
## Create your models here.
