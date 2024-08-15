from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.
def admin_console(request):
    menu_data = Product.objects.all()
    return render(request, 'products/menu.html', {'menu': menu_data})