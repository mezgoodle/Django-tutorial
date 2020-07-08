from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h4>Hello world</h4>')

def about(request):
    return HttpResponse('<h4>About us</h4>')