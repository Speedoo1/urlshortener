import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from base.models import short_link


def index(request):
    return render(request, "base/index.html")


def create(request):
    if request.method == 'POST':
        get_link = request.POST.get('link').replace('https://', '')
        uid = str(uuid.uuid4())[:5]
        link = short_link(link=get_link, shorten_link=uid)
        link.save()
        return HttpResponse(uid)


def go(request, shorten_link):
    url_details = short_link.objects.get(shorten_link=shorten_link)
    return redirect('https://' + url_details.link)
