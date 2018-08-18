from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.
def my(request):
    key = request.POST.get("key")
    mybtn = request.GET.get('mybtn')

    if key:
        p = Person(first_name=key)
        p.save()
    data = Person.objects.all()
    Person.objects.filter(first_name=request.GET.get('hid')).delete()
    #if (mybtn=="Done"):

    return render(request, "index.html", context={"list":data})
def test (request):
    key = request.POST.get("key")
    if key:
        p = Person(first_name=key)
        p.save()
    return HttpResponse("LOL")
