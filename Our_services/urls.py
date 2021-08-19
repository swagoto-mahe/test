from django.urls import path
from . import views

urlpatterns = [
    path('', views.services.as_view(), name='services'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
