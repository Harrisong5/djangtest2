from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page2(request):
    return HttpResponse("bigman")