from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import loader
def index(request):
    return HttpResponse("PORTFOLIO")
def htmlexample(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
def blog(request):
    template=loader.get_template('blog.html')
    return HttpResponse(template.render())
def read(request):
    template=loader.get_template('read.html')
    return HttpResponse(template.render({},request))
def resume(request):
    template=loader.get_template('resume.html')
    return HttpResponse(template.render())