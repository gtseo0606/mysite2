from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def TellHello(requests):
    html = "<h1> 가나다라마 </h1>"
    return HttpResponse(html)


