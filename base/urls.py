from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.homePage, name = "home"),
    path('project/<str:pk>/', views.projectPage, name = "project"),
    path('add-project/',views.addProject, name = 'add-project'),
    path('edit-project/<str:pk>/',views.editProject, name = 'edit-project'),
    path('inbox/', views.inboxPage, name = "inbox"),
    path('inbox/<int:pk>/', views.MessageDetail.as_view(), name='user_detail'),
]