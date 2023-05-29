from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("city", views.city, name="city"),
    path("article/<int:pk>", views.detailview, name="article_detail"),
    path("post", views.allposts, name="allposts"),
    path("category/<int:pk>", views.category, name="category"),
    path("search", views.search, name="search"),
    path("allcategories", views.allcategory, name="allcategory"),
    path("images", views.images, name="images"),

]

