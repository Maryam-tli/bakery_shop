from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from app_bakery.forms import *

# Create your views here.
def home_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print("PHONE VALUE:", request.POST.get('phone'))
            print(form.errors)
            return HttpResponse('Your Information Is Not Valid')
    form = BookingForm()
    return render(request, 'home.html', {'booking':form})

def about_view(request):
    return render(request, 'about-us.html')

def contact_view(request):
    return render(request, 'contact-us.html')