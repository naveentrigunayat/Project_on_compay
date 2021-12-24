from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Welcome),
    path('load_form', views.load_form),
    path('add', views.add)
]