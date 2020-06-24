from django.db import models

class CV(models.Model):
    name_surname = models.TextField(default='');
    address = models.TextField(default='');
    email = models.EmailField(default='');
    about_description = models.TextField(default='');
    
class JOB(models.Model):
    title = models.TextField(default='');
    company = models.TextField(default='');
    description = models.TextField(default='');
    dates = models.TextField(default='');

class EDUCATION(models.Model):
    institution = models.TextField(default='');
    title = models.TextField(default='');
    description = models.TextField(default='');
    grade = models.TextField(default='');
    dates = models.TextField(default='');
    
class INTERESTS(models.Model):
    description = models.TextField(default='');
    
class AWARDS(models.Model):
    award = models.TextField(default='');
    
#from django.db import models
#
#class Item(models.Model):
#    text = models.TextField(default='')
#
## Create your models here.
