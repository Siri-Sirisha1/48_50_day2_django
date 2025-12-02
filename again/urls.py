from django.urls import path
from .views import about,home,login,contact,register
urlpatterns=[
    path("about/",about), # link , view 
    path("",home),
    path("contact/",contact),
    path("login/",login),
    path("register/",register)
]