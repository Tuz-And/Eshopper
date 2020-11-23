from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')


def error(reqest):
    return render(reqest,"pages/404.html")


def contact_us(reqest):
    return render(reqest,"pages/contact-us.html")


