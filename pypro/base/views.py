from django.http import HttpResponse


def home(request):
    # raise ValueError('test error..')
    return HttpResponse('<html><body>Hola Django</body></html>')
