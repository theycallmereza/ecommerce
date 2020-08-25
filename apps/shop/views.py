from django.shortcuts import render
from django.views import generic
from .models import Product


# Create your views here.

class HomepageView(generic.ListView):
    context_object_name = 'products'
    template_name = 'index.html'

    def get_queryset(self):
        return Product.objects.all()
