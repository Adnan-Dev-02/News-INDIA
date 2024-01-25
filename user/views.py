from django.db.models import Q
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    d=slider.objects.all().order_by('-id')[0:3]
    nc=ncategory.objects.all()
    x=mynews.objects.all().order_by('-id')[0:6]
    vdata=videonews.objects.all().order_by("-id")
    ct=city.objects.all().order_by('-id')
    mydict={'data': d, 'data2': nc, 'ndata':x, 'vdata': vdata, 'city': ct}
    return render(request, 'user/index.html', context=mydict)

def gallery(request):
    d=igallery.objects.all().order_by("-id")
    mydict={"data": d}
    return render(request, 'user/gallery.html', context=mydict)

def about(request):
    return render(request, 'user/about.html')

def contact(request):
    status=False
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mob')
        message=request.POST.get('msg')
        contactus(Name=name,Email=email,Mobile=mobile,Message=message).save()
        status=True

    return render(request, 'user/contact.html', context={"msg":status})

def video(request):
    vdata=videonews.objects.all().order_by("-id")
    if request.method == "GET":
        s=request.GET.get("search")
        if s is not None:
            vdata=videonews.objects.all().filter(Q(vhead__icontains=s) | Q(vcategory__icontains=s) | Q(vcity__icontains=s))

        print(s)
    md={"data": vdata}
    return render(request, 'user/video.html', md)

def news(request):
    x = ncategory.objects.all().order_by("-id")
    y = city.objects.all().order_by("-id")
    z = mynews.objects.all().order_by("-id")
    ctid = request.GET.get('ctid')
    catid = request.GET.get('catid')
    if ctid is not None:
        z = mynews.objects.all().filter(ncity=ctid)
    elif catid is not None:
        z = mynews.objects.all().filter(category=catid)
    mydict = {"cat": x, "ct": y, "news": z}
    return render(request, 'user/news.html', mydict)

def ndetails(request):
    nid=request.GET.get('n')
    x = mynews.objects.all().filter(id=nid)
    mydict = {"ndata": x}
    return render(request, 'user/ndetails.html', mydict)

def viewnews(request):
    a=request.GET.get('msg')
    c=request.GET.get('cid')
    x=""
    if(a is not None):
        x=mynews.objects.all().filter(category=a).order_by("-id")
    elif(c is not None):
        x=mynews.objects.all().filter(ncity=c).order_by("-id")
    mydict = {"ndata": x}
    return render(request, 'user/viewnews.html', mydict)

def vdetails(request):
    a=request.GET.get('vid')
    x=videonews.objects.all().filter(id=a)
    myd={'vdata':x}
    return render(request, 'user/vdetail.html', myd)