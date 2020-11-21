from django.http import HttpResponse


def trigger_error(request):
    division_by_zero = 1 / 0


def home(request):
    return HttpResponse('<html><body>Hola Django</body></html>')
