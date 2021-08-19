from django.urls import path
from . import views

urlpatterns = [
    path('',views.homelist.as_view, name='homelist'),
    
]   