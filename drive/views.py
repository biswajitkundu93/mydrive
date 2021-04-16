from django.shortcuts import render
from drive.user.models import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json,os
from django.http import HttpResponse


def home(request):
    try:
        if request.session.get("username",False):
            user = UserRegistor.objects.get(id=request.session["user_id"])
            user.is_logging="1"
            rootFolder = RootFolderRecord.objects.get(user=user,is_deleted="0")
            folderList = [{
                "id":i.id,
                "name":i.child
            }for i in AllFolderRecord.objects.filter(parent=rootFolder.rootfolder,is_deleted="0")]
            data  = {
                "name":user.name,
                "folderList":folderList
            }
            print(data)
        return render(request, 'drive/home.html',data)
    except Exception as e:
        print(e)
        print("not found")
        data={
            "name":False
        }
        print(data)
        return render(request, 'drive/home.html',data)

@csrf_exempt
def createFolder(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data["name"])
        try:
            user= UserRegistor.objects.get(id=request.session["user_id"])
            parent = RootFolderRecord.objects.get(user=user,is_deleted="0")
            newFolder = AllFolderRecord.objects.create(
                user=user,
                parent = parent.rootfolder,
                child = data['name'],
                is_deleted="0"
            )
            newFolder.save()
            return HttpResponse(json.dumps({"status": 1}), content_type='application/json')
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"status": 0}), content_type='application/json', status=401)
    else:
        print("error")
        return HttpResponse(json.dumps({"status": 0}), content_type='application/json', status=401)

@csrf_exempt
def openFolder(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user= UserRegistor.objects.get(id=request.session["user_id"])
            if int(data["id"]) >0:
                parent = AllFolderRecord.objects.get(user=user,id=data['id'],is_deleted="0")
                folderList = [{
                    "id":i.id,
                    "name":i.child
                }for i in AllFolderRecord.objects.filter(parent=parent.child,is_deleted="0")]
                parent_obj = {
                    "id":parent.id,
                    "name":parent.parent
                }
            else:
                rootFolder = RootFolderRecord.objects.get(user=user,is_deleted="0")
                folderList = [{
                    "id":i.id,
                    "name":i.child
                }for i in AllFolderRecord.objects.filter(parent=rootFolder.rootfolder,is_deleted="0")]
                parent_obj={
                    "id":0,
                    "name":rootFolder.rootfolder
                }
            data = {
                "folderList":folderList,
                "parent":parent_obj
            }
            return HttpResponse(json.dumps({"status": 1, "data":data}), content_type='application/json')
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"status": 0}), content_type='application/json', status=401)
    else:
        print("error")
        return HttpResponse(json.dumps({"status": 0}), content_type='application/json', status=401)
