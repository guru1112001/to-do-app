from django.urls import path, include
from . import views
app_name = "notes"

urlpatterns = [
    path("", views.home_view, name="homepage"),


]
