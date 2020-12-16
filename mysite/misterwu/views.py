from django.shortcuts import render
import requests
import json
from django.views.generic import View
from django.http import JsonResponse
from .models import Teacher,Course,Student,TeacherAssistant
# Create your views here.

def home(request):
    api_request = requests.get("https://api.github.com/users?since=0")
    api = json.loads(api_request.content)
    return render(request,'home.html',{"api":api})

def user(request):
    if request.method == 'POST':
        user = request.POST['user']
        user_request = requests.get("https://api.github.com/users/"+user)
        username = json.loads(user_request.content)
        return render(request,'user.html',{"user":user,"username":username})
    else:
        notfound = "请在搜索框中输入您需要查询的用户"
        return render(request, 'user.html', {'notfound':notfound})


def teacher(request):
    teacher = Teacher.objects.all()
    # print(teacher)
    teacher2 = Teacher.objects.get(nickname='mango')
    # print(teacher2,type(teacher2))
    teacher3 = Teacher.objects.filter(fans_gte='m')
    print(teacher3)

    return render(request,'teacher.html',{})