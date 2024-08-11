from django.http import HttpResponse


def home(request):
    user = request.user
    return HttpResponse("<h1>Welcome user!  <br> How are you doing today, {}?</h1>".format(user))