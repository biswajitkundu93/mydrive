from django.shortcuts import render
from drive.user.models import *

def home(request):
    try:
        if request.session.get("username",False):
            user = UserRegistor.objects.get(id=request.session["user_id"])
            user.is_logging="1"
            data  = {
                "name":user.name,
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