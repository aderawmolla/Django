from django.shortcuts import render

from django.http import HttpResponse
from .models import Product


def index(request):
    products= Product.objects.all()# all-returns all ,filter(somecondition),get()-single product,save()-to save to database,

    return render(request,'index.html',{"products":products})#key-value pair to be passed to index.html

# Create your views here.
