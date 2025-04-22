from django.http import HttpResponse
from django.shortcuts import render

#Create your views here.
def home(request):
    #return HttpResponse("Hello, Django! This is the home page.")
    return render(request,'website/index.html')
#Create about page view function
def about(request):
    return render(request, 'website/about.html')
def dark(request):
    return render(request, 'website/aboutdark.html')


#Create contact page view function
def contact(request):
    return HttpResponse("This is the contact page. Here you can contact us. This page is dedicated to Contact Page.")

def services(request):
    return HttpResponse("This is the services page.")