from django.shortcuts import render
from testapp.models import hydjobs,bangjobs,punejobs
# Create your views here.
def home_view(request):
    return render(request,"testapp/home.html")

def hyd_view(request):
    data=hydjobs.objects.all()
    return render(request,"testapp/hyderbad.html",context={"data":data,"heading":"Hyderbad Jobs Information..."})

def pune_view(request):
    data=punejobs.objects.all()
    return render(request,"testapp/pune.html",context={"data":data,"heading":"Pune Jobs Information..."})

def banglore_view(request):
    data=bangjobs.objects.all()
    return render(request,"testapp/bangalore.html",context={"data":data,"heading":"Bangalore Jobs Information..."})