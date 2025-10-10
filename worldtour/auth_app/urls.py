from django.urls import path
from . import views

# Define a list of url patterns
urlpatterns = [
    path('', views.home_view, name='auth'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
]
