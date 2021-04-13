from django.db import models
from datetime import datetime

# Create your models here.
class UserRegistor(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    password = models.CharField(max_length=255,null=True,blank=True)
    ip = models.CharField(max_length=255,null=True,blank=True)
    system = models.CharField(max_length=255,null=True,blank=True)
    username = models.CharField(max_length=255,null=True,blank=True)
    browser = models.CharField(max_length=255,null=True,blank=True)
    is_logging = models.CharField(max_length=255,null=True,blank=True)
    is_deleted = models.CharField(max_length=255,null=True,blank=True)
    is_admin = models.CharField(max_length=255,null=True,blank=True)
    created_by = models.DateTimeField(default=datetime.now)
    updated_by = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'user_register'
        ordering = ['id']

    def __str__(self):
        return self.name



class Logging_history(models.Model):
    username = models.CharField(max_length=255,null=True,blank=True)
    ip = models.CharField(max_length=255,null=True,blank=True)
    system = models.CharField(max_length=255,null=True,blank=True)
    browser = models.CharField(max_length=255,null=True,blank=True)
    logging_time = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'logging_history'
        ordering = ['id']

    def __str__(self):
        return self.username

    