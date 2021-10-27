from django.urls import path, include
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('user_records/', views.user_records, name='user_records'),
    path('', views.base, name='base'),
]
