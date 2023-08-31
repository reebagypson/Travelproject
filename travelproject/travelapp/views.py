from django.shortcuts import render
from .models import place
from .models import team

# Create your views here.
def index(request):
    obj1=place.objects.all()
    obj2=team.objects.all()
    return render(request,"index.html",{'result1':obj1})
