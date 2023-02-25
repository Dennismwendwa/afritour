from django.urls import path
from .views import DetailView, Allposts, CategoryView
from . import views




urlpatterns = [
    path("", views.home, name="home"),
    path("city", views.city, name="city"),
    path("article/<int:pk>", DetailView.as_view(), name="article_detail"),
    path("post", Allposts.as_view(), name="allposts"),
    path("category/<str:cats>", CategoryView, name="category"),

]
