from django.urls import path
from .views import*

urlpatterns = [
    path('app1/', home, name='home')
]