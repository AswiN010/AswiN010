from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, person


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    ear=person.objects.all()
    return render(request, "index.html",{'result':obj,'res':ear})

