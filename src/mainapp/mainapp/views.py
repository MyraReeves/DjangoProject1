from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    user = request.user
    products1 = ["Coffee", "Tea", "Fruit juices", "Hard-boiled eggs", "Cereal", "Yogurt", "English muffins", "Bagels", "Cream cheese", "Assorted jams/jellies", "Oatmeal", "Apples, Oranges, or Bananas"]
    context = {
        'user': user,
        'breakfastProducts':  products1,
    }
    return render(request, "home.html", context)