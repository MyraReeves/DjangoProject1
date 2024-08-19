from django.forms import ModelForm
from .models import Product


# Create a class object (classes start with a capital letter) named ProductForm, inheriting from the class ModelForm:
class ProductForm(ModelForm):
    class Meta:
        # Create a variable to hold the class "Product":
        model = Product
        
        # Have the fields be all the "Product" fields (type, name, description, price, and image) using a dunder:
        fields = '__all__'
