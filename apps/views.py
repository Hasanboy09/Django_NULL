from django.shortcuts import render
from django.views.generic import TemplateView


from django.http import HttpResponse

def hello_world_view(request):
    return HttpResponse("Hello, World!")

