from django.shortcuts import render
from django.db import models
from okeadminıu.models import PortfoyloModel

def Anasayfa(request):
    projeler = PortfoyloModel.objects.all()
    return render(request,"pages/anasayfa.html", context={
        "projeler":projeler,
    })