from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product


# Define all needed methods/views below.
# Reminder: methods start with lowercase letters.


def admin_console(request):
    menu_data = Product.objects.all()
    return render(request, 'products/menu.html', {'menu': menu_data})

# ________________________________________________________________________________________


def details(request, pk):       # pk stands for primary key.

    # Convert the string value of the primary key into a numeric integer:
    pk = int(pk)

    # Query the database and store in a variable the database record (from within the Product model) associated with the requested primary key (pk is a dictionary object).
    # If it doesn't exist, return a 404 error:
    item = get_object_or_404(Product, pk=pk)

    # Store in a variable the information from the POST request. Make the instance equal to the above-created variable.
    # If information can't be retrieved, set a value of None:
    form1 = ProductForm(data=request.POST or None, instance=item)

    if request.method =='POST':

        # Check if new info the user has entered for a menu item has correct format. If so, then save the modifications to the database:
        if form1.is_valid():
            form2 = form1.save(commit=False)
            form2.save()
            return redirect('admin_console')

        else:
            print(form1.errors)

    # Render the form information from the database of the requested item onto an HTML page for the user to see:
    else:
        return render(request, 'products/food_item.html', {'form': form1})

# ________________________________________________________________________________________


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
    context = {"item": item}
    return render(request, "products/confirmDelete.html", context)

# ________________________________________________________________________________________


def confirmedDelete(request):
    if request.method == 'POST':
        # Create form
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('admin_console')
    else:
        return redirect('admin_console')
