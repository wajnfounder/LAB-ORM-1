from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("create/", views.create_post_view, name="create_post"),
    path("delete/<int:id>/", views.delete_post_view, name="delete_post"),
path("edit/<int:id>/", views.edit_post_view, name="edit_post"),
]

