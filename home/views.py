from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
def index(request):
    # return HttpResponse("This is HomePage")
    products = Product.objects.all()
    return render(request, 'index.html', 
                  {'products': products})

def categories(request):
    # return HttpResponse("This is categories page")
    return render(request, 'category.html')

def shop(request):
    # return HttpResponse("This is shop page")
    products = Product.objects.all()
    return render(request, 'shop.html', 
                  {'products': products})

def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("This is contact page")
    return render(request, 'contact.html')
