from django.http import HttpResponse

#Create your views here.
def home(request):
    return HttpResponse("Hello, Django! This is the home page.")

#Create about page view function
def about(request):
    return HttpResponse("This is the about page. Here you can Learn about us. This page is dedicated to About Page.")

#Create contact page view function
def contact(request):
    return HttpResponse("This is the contact page. Here you can contact us. This page is dedicated to Contact Page.")

def services(request):
    return HttpResponse("This is the services page.")