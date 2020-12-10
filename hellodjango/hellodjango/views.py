from django.http import HttpResponse
from django.shortcuts import render



def hello(request):
    return HttpResponse("hello world!")

def runoob(request):
    context = {}
    context['hello'] = 'hello apple!'
    return render(request,'runoob.html',context)


