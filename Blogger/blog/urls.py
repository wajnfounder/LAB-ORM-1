from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("create/", views.create_post_view, name="create_post"),
]

