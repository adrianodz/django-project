from django.http import HttpResponse


# def trigger_error(request):
#     division_by_zero = 1 / 0
from django.shortcuts import render


def home(request):
    #return HttpResponse('<html><body>Hola Django</body></html>')
    return render(request, 'base/home.html')