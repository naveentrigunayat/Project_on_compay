
from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
    path('category/<int:id>/',v.get_by_category,name="get_by_category"),
    path('search',v.search_product,name="search"),
]
