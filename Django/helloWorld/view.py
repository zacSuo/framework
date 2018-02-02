#from django.http import HttpResponse


 
from django.shortcuts import render
def hello(request):
    context = {}
    context['hello'] = "hellow world!"
    context['a']=30
    context['c']=30
    context['d']=30
    context['name']="DD  dsdf你"
    return render(request,'hello.html', context)
    #return HttpResponse("Hello world!")
