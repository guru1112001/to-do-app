
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("user.urls")),
    path("login/",auth_views.LoginView.as_view(template_name="user/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(template_name="user/logout.html"),name="logout"),
    path("",include("notes.urls")),
]
