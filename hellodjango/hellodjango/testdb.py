from django.http import HttpResponse

from TestModel.models import Test

#添加
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

#查询
def getdata(request):
    response = ""
    response1 = ""

    list = Test.objects.all()
    response2 = Test.objects.filter(id=1)

    response3 = Test.objects.get(id=1)

    Test.objects.order_by('name')[0:2]

    Test.objects.order_by("id")

    Test.objects.filter(name='runoob').order_by("id")

    for var in list:
        response1 += var.name + " "
    response = response1

    return HttpResponse("<p>" + response + "</p>")

#更新
def updatedb(request):
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()

    return HttpResponse('<p>修改成功</p>')

#删除
def deletedb(request):
    test1 = Test.objects.get(id=1)
    test1.delete()

    return HttpResponse('<p>删除成功</p>')