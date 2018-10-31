from django.http import HttpResponse


def mainPage(request):
    return HttpResponse("Hello, world. You're at the app main page.")