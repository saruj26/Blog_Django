from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index , name="index"),
    path("post/<str:slug>", views.detail , name="detail"),

    path("new_somthing_url", views.new_url_view , name="new_page_url"),
    path("old_url", views.old_url_redirect , name="old_url"),


    path("contact", views.contact, name="contact"),
    path("about", views.about , name="about"),

    path("register", views.register , name="register"),
    path("login", views.login , name="login"),

    path("dashboard" , views.dashboard , name = "dashboard"),
    path("logout" , views.logout , name ="logout"),
    path("forgot_password", views.forgot_password  , name ="forgot_password" ),
    path("reset_password/<uidb64>/<token>", views.reset_password  , name ="reset_password" ),


]
