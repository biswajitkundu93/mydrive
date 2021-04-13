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
            print(user)
            request.session["username"]=user.username
            request.session["user_id"]=user.id
            user.save()
            return HttpResponse(json.dumps({"status": 1}), content_type='application/json')
        except :
            return HttpResponse(json.dumps({"status": 0}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({"status": 0}), content_type='application/json')

def logout(request):
    return HttpResponse(json.dumps({"status": 0}), content_type='application/json')


