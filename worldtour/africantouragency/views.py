from django.shortcuts import render, redirect
from .models import Tour
from .forms import ContactForm
# Create your views here.


def index(request):
    tours = Tour.objects.all()
    context = {'tours': tours}
    return render(request, 'tours/index.html', context)


def styling(request):
    return render(request, 'django_app/index.html')


# *******************************************
# FORMS APP

# Home page for the form app
def home_view(request):
    return render(request, 'form_app/home.html')


# handle the contact form
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'form_app/contact.html', context)


# define the contact success page
def contact_success_view(request):
    return render(request, 'form_app/success.html')


# *****************************
