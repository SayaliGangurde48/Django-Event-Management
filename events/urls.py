from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_event, name='upload_event'),
]