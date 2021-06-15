from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.homePage, name = "home"),
    path('project/<str:pk>/', views.projectPage, name = "project")
]