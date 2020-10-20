from django.shortcuts import HttpResponse

# Create your views here.
def index(req):
    return HttpResponse("Hello, world!")