from django.urls import path

from . import views
from apirequests import views as apiviews

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('query/', views.query, name='query'),
    path('studentsfromcourse/', apiviews.studentsFromCourse, name='studentsFromCourse')
]