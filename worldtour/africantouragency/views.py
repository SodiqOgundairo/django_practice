from django.shortcuts import render
from .models import Tour


# Create your views here.


def index(request):
    tours = Tour.objects.all()
    context = {'tours': tours}
    return render(request, 'tours/index.html', context)


def styling(request):
    return render(request, 'django_app/index.html')
