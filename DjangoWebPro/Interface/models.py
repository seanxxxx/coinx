from django.db import models

# Create your models here.

class Interface(models.Model):
    interface_name = models.CharField(max_length=64)
    interface_method = models.CharField(max_length=8)
    interface_desc = models.CharField(max_length=64)
    interface_address = models.CharField(max_length=64)
    interface_param = models.CharField(max_length=128)
    interface_format = models.CharField(max_length=8)