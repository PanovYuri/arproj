from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import ArObj, Media

# Create your views here.
def index(req):
    latest_ar_projects_list = ArObj.objects.order_by('-date')[:5]
    context = {'latest_list' : latest_ar_projects_list}
    return render(req, 'arscanner/index.html', context)

def details(req, ar_id):
    arobj = get_object_or_404(ArObj, pk=ar_id)
    return render(req, 'arscanner/details.html', {'arobj':arobj})

def scanning(req, ar_id):
    arobj = get_object_or_404(ArObj, pk=ar_id)
    return render(req, 'arscanner/scann.html', {'media':arobj.media})