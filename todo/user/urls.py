from django.urls import path,include
from . import views
app_name="user"

urlpatterns = [
    path("login/",views.login_view,name="loginpage"),

]