from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>Learn Interactively</title></html>')