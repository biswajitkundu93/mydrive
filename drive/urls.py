from django.urls import path,include
from . import templating
from . import views

urlpatterns = [
    path("",templating.home, name="home"),
    path("user/",include("drive.user.urls"))
]
