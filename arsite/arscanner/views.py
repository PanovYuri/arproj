from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import ArObj, Media
from .forms import CardForm, FileUploadForms

# Create your views here.
def index(req):
    latest_ar_projects_list = ArObj.objects.order_by('-date')[:5]
    context = {'latest_list' : latest_ar_projects_list}
    return render(req, 'arscanner/index.html', context)

def details(req, ar_uuid):
    arobj = get_object_or_404(ArObj, unique_id=ar_uuid)
    return render(req, 'arscanner/details.html', {'arobj':arobj})

def scanning(req, ar_uuid):
    arobj = get_object_or_404(ArObj, unique_id=ar_uuid)
    return render(req, 'arscanner/scann.html', {'media':arobj.media})

def append_card(req):
    if req.method == "GET":
        card = CardForm
        fileForm = FileUploadForms()
        return render(req, 'arscanner/appendcard.html', {"form": card, "fileform": fileForm})
    else:
        title = req.POST.get('title')
        description = req.POST.get('description')
        url = req.POST.get('url')
        date_event = req.POST.get('title')
        media = req.POST.get('media')

        mediaObj = Media('test', media)
        mediaObj.save()
        arObj = ArObj(title=title, description=description, url=url, date_event=date_event, media=media)