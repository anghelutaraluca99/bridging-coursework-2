from django.db import models

class CV(models.Model):
    name_surname = models.TextField(default='');
    address = models.TextField(default='');
    email = models.EmailField(default='');
    about_description = models.TextField(default='');
    


#from django.db import models
#
#class Item(models.Model):
#    text = models.TextField(default='')
#
## Create your models here.
