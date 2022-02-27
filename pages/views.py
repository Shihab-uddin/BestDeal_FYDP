import imp
from django.shortcuts import render
from django.http import HttpResponse, request

from products.models import Product

# Create your views here.

def home_view(request,*args, **kwargs):
    return render(request, "homepage.html", {})


def searchresult_view(request,*args, **kwargs):
    if request.method == 'GET':
        search = request.GET.get('search')
        #print(search)
        product = Product.objects.all().filter(productname__icontains=search)    
    context = {
        "object_list" : product, 
        'search' : search
    }
        
    return render(request, "searchresult.html", context)