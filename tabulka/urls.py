from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_record, name='create_record'),
]