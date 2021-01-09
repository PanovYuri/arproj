from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import ArObj, Media
from .forms import CardForm, FileUploadForms

def get_val_or_none(val):
    if val.rstrip() == "":
        return None
    else:
        return val

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
        # TODO: Добавить выборку по уровню подступа
        medias = Media.objects.all()
        return render(req, 'arscanner/appendcard.html', {"form": card, "fileform": fileForm, "medias": medias})
    else:
        title = req.POST.get('title')
        description = req.POST.get('description')
        url = req.POST.get('url')
        date = req.POST.get('date')
        time = req.POST.get('time')
        media = get_object_or_404(Media, pk=req.POST.get('media'))
        arObj = ArObj()
        arObj = ArObj(
            title=title,
            media=media)
        if url.rstrip() != "":
            arObj.url = url
        if date.rstrip() != "":
            if time.rsplit() == "":
                time = "00:00:00"
            arObj.date_event = "{} {}".format(date, time)
        if description.rstrip() != "":
            arObj.description = description
        arObj.save()
        # print(title, description, url, date, time, req.POST.get('media'))
        return render(req, 'arscanner/savecompleted.html')