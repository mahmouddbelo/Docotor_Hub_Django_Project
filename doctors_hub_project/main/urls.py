from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_results, name='search_results'),
    path('doctor/<int:doctor_id>/', views.doctor_details, name='doctor_details'),
]