from django.urls import path, include
from . import views
app_name = "notes"

urlpatterns = [
    path("", views.home_view, name="homepage"),
    path("about/",views.about_view,name="aboutpage"),
    path("create/",views.todo_create_view,name="create-todo"),
    path("update_todo/<int:pk>/",views.update_todo,name="update-todo"),
    path("delete_todo/<int:pk>/",views.delete_todo,name="delete-todo"),



]
