from django.shortcuts import render,get_object_or_404
from django.db import models
from okeadminıu.models import PortfoyloModel

def DetaySayfası(request,id):
    projeler = get_object_or_404(PortfoyloModel, id=id)
    return render(request,"pages/details.html", context={
        "projeler":projeler,
    })