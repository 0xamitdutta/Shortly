from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        long_url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        short_url = Url(long_url=long_url, uuid=uid)
        short_url.save()
        return HttpResponse(uid)

def go(request, key):
    url_details = Url.objects.get(uuid=key)
    return redirect(url_details.long_url)