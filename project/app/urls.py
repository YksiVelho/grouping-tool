from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('teacher/', views.teacherView, name='teacherView'),
]
