# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from TestModel.models import Test

# 数据库操作


def testdb(request):
    for i in range(1, 100):
        test1 = Test(name='runoob'+i)
        test1.save()

    return HttpResponse(json.dumps({'name': 'runoob'}), content_type='application/json')


def add(request):
    for i in range(1, 101):
        test1 = Test(name='zhangsan'+str(i))  # 修改这里，将整数转换为字符串
        test1.save()
    data = Test.objects.count()  # 使用count()方法获取添加的记录数

    return JsonResponse({
        'data': data,
        'success': True,
    }, safe=False)


def getAll(request):
    data = list(Test.objects.all().values())
    return JsonResponse({
        'data': data,
        'suceess': True,
        'msg': '成功',
        'code': 200
    }, safe=False)


@require_GET
def find(request):
    if request.method == 'GET':
        name = request.GET.get('name')  # 获取GET请求中的name参数
    else:
        name = None

    if name:
        data = list(Test.objects.filter(name=name).values()[0:1])
        response_data = {
            'data': data,
            'success': True,
            'msg': '成功',
            'code': 200
        }
    else:
        response_data = {
            'success': False,
            'msg': '未提供name参数',
            'code': 400
        }

    return JsonResponse(response_data)
