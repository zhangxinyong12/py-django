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
    # for i in range(1, 101):
    #     test1 = Test(name='zhangsan'+str(i))  # 修改这里，将整数转换为字符串
    #     test1.save()
    # data = Test.objects.count()  # 使用count()方法获取添加的记录数

    # 使用 bulk_create() 方法可以提高性能，因为它减少了与数据库的交互次数。这对于批量创建大量对象时非常有用。
    objects_to_create = [Test(name=f'zhangsan{i}') for i in range(1, 101)]
    Test.objects.bulk_create(objects_to_create)

    data = len(objects_to_create)

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

# 更新


def update(request):
    id = request.GET.get('id')
    name = request.GET.get('name')

    data = Test.objects.get(id=id)
    data.name = name
    data.save()
    return JsonResponse({
        'data': list(Test.objects.filter(id=id).values()),
        'success': True,
    }, safe=False)


# 删除
def delete(request):
    id = request.GET.get('id')
    data = Test.objects.filter(id=id)
    res = {}
    if data:
        data.delete()
        res = {
            'success': True,
            'msg': '删除成功',
        }
    else:
        res = {
            'msg': '数据不存在',
        }
    return JsonResponse(res, )
