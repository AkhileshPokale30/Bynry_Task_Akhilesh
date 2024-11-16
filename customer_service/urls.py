# customer_service/urls.py

from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views  # Add this import
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Ensure this line points to the dashboard view
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='customer_service/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('submit-request/', views.submit_service_request, name='submit_service_request'),
    path('request/<int:pk>/', views.service_request_detail, name='service_request_detail'),

]
