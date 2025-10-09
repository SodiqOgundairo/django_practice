from django.urls import path
from . import views

# Define a list of url patterns
urlpatterns = [
    path('', views.home_view, name='auth'),
    path('/auth/login/', views.login_view, name='login'),
    path('/auth/register/', views.register_view, name='register'),
    path('/auth/logout/', views.logout_view, name='logout'),
    path('/auth/protected/', views.ProtectedView.as_view(), name='protected'),
]
