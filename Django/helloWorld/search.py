# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render

#表单
def search_form(request):
    return render_to_response('search_form.html')


#接受请求数据
def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = 'content:'+ request.GET['q']
    else:
        message = 'send empity'

    return HttpResponse(message)


def search_post(request):
    ctx = {}
    if request.method == 'POST':
        ctx['rlt'] = request.POST['q']

    return render(request, "post.html", ctx)
