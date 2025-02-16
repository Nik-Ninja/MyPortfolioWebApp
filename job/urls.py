from django.urls import path

from . import views

urlpatterns = [
    path('', views.alljobs, name='all-jobs')
]