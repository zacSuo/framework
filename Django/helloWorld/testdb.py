# -*- coding:utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test1

# 数据库操作

def addItem(request):
    test1 = Test1(name="runoob3")
    test1.save()
    return HttpResponse("success成功")

def getDb(request):
    response = ""
    response1 = ""

    list = Test1.objects.all()

    response2 = Test1.objects.filter(name="runoob").order_by('id')[1:4]

    for item in response2:
        response1 += item.name + " , "

    response = response1

    return HttpResponse("<p>" + response + "</p>")


def updateItem(request):
    test1 = Test1.objects.get(id=2)
    test1.name = "gggggg"
    test1.save()


    Test1.objects.filter(id=3).update(name="daaaaaaa")

    return HttpResponse("成功")


def deleteItem(request):
    test1 = Test1.objects.get(id=2)
    test1.delete()

    Test1.objects.filter(id=1).delete()
    return HttpResponse("success")
