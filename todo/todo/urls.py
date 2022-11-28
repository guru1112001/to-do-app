
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",include("user.urls")),
    path("login/",include("user.urls")),
    path("",include("user.urls")),
]
