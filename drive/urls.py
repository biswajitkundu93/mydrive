from django.urls import path
from . import templating
from . import views

urlpatterns = [
    path("",templating.home, name="home")
]
