from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("create-folder",views.createFolder, name="create-folder"),
    path("open-folder",views.openFolder, name="open-folder"),
    path("user/",include("drive.user.urls"))
]
