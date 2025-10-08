from django.urls import path
from . import views

# Define a list of url patterns
urlpatterns = [
    path('', views.index, name='home'),
    # path('home', views.inde),
    path('styling/', views.styling),
    path('form-home/', views.home_view, name='form-app'),
    path('contact/', views.contact_view, name='contact'),
    path('contact-success/', views.contact_success_view, name='contact-success'),
]
