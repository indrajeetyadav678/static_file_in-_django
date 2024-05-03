from django.urls import path
from .views import*

urlpatterns = [
    path('app2/', home1, name='home')
]