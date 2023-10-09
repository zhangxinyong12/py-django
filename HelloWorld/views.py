from django.http import HttpResponse
import json
from django.shortcuts import render


def hello(request):
    return HttpResponse('1111111111')


def render_json(request):
    return HttpResponse(json.dumps({'name': 'zhangsan'}), content_type='application/json')


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)
