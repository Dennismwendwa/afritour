from django.urls import path
from . import views 


urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('contant', views.contant, name="contant"),
]
