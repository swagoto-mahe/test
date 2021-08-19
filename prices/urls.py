from django.urls import path
from . import views

urlpatterns = [
    path('', views.prices.as_view(), name='prices'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
