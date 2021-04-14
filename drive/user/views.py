from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json
from Mydrive.middelware import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def signup(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        # browser = (request.user_agent.browser.family + request.user_agent.browser.version_string)
        # os = (request.user_agent.os.family + request.user_agent.os.version_string)
        ip = get_client_ip(request)
        try:
            newUser = UserRegistor.objects.create(
                name = data['name'],
                email = data['email'],
                password = data['password'],
                ip = str(ip),
                system = "os",
                username = data['email'],
                browser = "browser",
                is_logging = "0",
                is_deleted = "0",
                is_admin = "0"
            )
            request.session["username"]=newUser.username
            request.session["user_id"]=newUser.id
            newUser.save()
            return HttpResponse(json.dumps({"status": 1}), content_type='application/json')
        except Exception as e:
            return HttpResponse(json.dumps({"status": 0}), content_type='application/json', status=401)
    else:
        return HttpResponse(json.dumps({"status": 0}), content_type='application/json', status=401)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user= UserRegistor.objects.get(username=data["username"],password=data["password"])
            request.session["username"]=user.username
            request.session["user_id"]=user.id
            user.save()
            return HttpResponse(json.dumps({"status": 1}), content_type='application/json')
        except :
            return HttpResponse(json.dumps({"status": 0}), content_type='application/json', status=401)
    else:
        return HttpResponse(json.dumps({"status": 0}), content_type='application/json', status=401)

@csrf_exempt
def logout(request):
    if request.method == 'POST':
        try:
            if  request.session["username"]:
                user= UserRegistor.objects.get(id=request.session["user_id"])
                user.is_logging="0"
                user.save()
                del request.session["username"]
                del request.session["user_id"]
                return HttpResponse(json.dumps({"status": 1}), content_type='application/json')
            else:
                print("error1")
                return HttpResponse(json.dumps({"status": 0}), content_type='application/json', status=401)
        except Exception as e :
            print(e)
            return HttpResponse(json.dumps({"status": 0}), content_type='application/json', status=401)
    else:
        print("error2")
        return HttpResponse(json.dumps({"status": 0}), content_type='application/json', status=401)

