from django.db import models
from drive.user.models import *

# Create your models here.
class RootFolderRecord(models.Model):

    user = models.ForeignKey(UserRegistor, on_delete=models.CASCADE)
    rootfolder = models.CharField(max_length=255,null=True,blank=True)
    is_deleted = models.CharField(max_length=255,null=True,blank=True)
    created_by = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'all_root_folder_record'
        ordering = ['id']

    def __str__(self):
        return self.rootfolder
    
class AllFolderRecord(models.Model):
    
    user = models.ForeignKey(UserRegistor, on_delete=models.CASCADE)
    parent = models.CharField(max_length=255,null=True,blank=True)
    child = models.CharField(max_length=255,null=True,blank=True)
    is_deleted = models.CharField(max_length=255,null=True,blank=True)
    created_by = models.DateTimeField(default=datetime.now)

    

    class Meta:
        db_table = 'all_folder_record'
        ordering = ['id']

    def __str__(self):
        return self.folder

class AllFiles(models.Model):
    user = models.ForeignKey(UserRegistor, on_delete=models.CASCADE)
    parent = models.CharField(max_length=255,null=True,blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    path = models.CharField(max_length=255,null=True,blank=True)
    is_deleted = models.CharField(max_length=255,null=True,blank=True)
    created_by = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'all_file_record'
        ordering = ['id']

    def __str__(self):
        return self.name