from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from members.forms import Image_galleryForm
from members.models import Image_gallery,Upcoming_event,News_gallery
from members.forms import *
from django.forms import inlineformset_factory
from members.decorator import *

def addimagesG(request):

    form = Image_galleryForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form=Image_galleryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('members_home')

    return render(request, 'members/Image_gallery.html' ,context )

def viewImages(request):

    Images = Image_gallery.objects.all()[:1]
    context={'img':Images}
    return render(request,'members/test.html',context)

