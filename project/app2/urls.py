from django.urls import path
from .views import*

urlpatterns = [
    path('app2/', home, name='home')
]