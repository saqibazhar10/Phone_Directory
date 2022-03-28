from django.urls import path
from . import views


urlpatterns= [
    path("", views.login,name="login"),
    path("register/", views.register,name="register"),
    path("homepage/", views.homepage,name="homepage"),
    path("all_contact/", views.all_contact ,name="all_contact"),
    path("update/", views.update ,name="update"),
    
]