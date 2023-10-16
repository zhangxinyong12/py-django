import json
import time
from UserModel.models import User
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
#  user数据库操作

# 新增用户


def add(req):
    objects_to_create = [
        User(name=f'zhangsan{i}', age=i, sex=i % 2) for i in range(1, 101)]
    User.objects.bulk_create(objects_to_create)
    dataLen = len(objects_to_create)
    return JsonResponse({
        'data': dataLen,
        'success': True,
    }, safe=False)


# 查询

def getList(req):
    allList = User.objects.all()
    dataLen = len(allList)
    return JsonResponse({
        'data': list(allList.values()),
        'length': dataLen,
        'success': True,
    }, safe=False)


# 根据条件查询

def findBy(req):
    if req.method == 'GET':
        name = req.GET.get('name')
        id = req.GET.get('id')
    else:
        name = None
        id = None

    if name or id:
        query = Q()
        if name:
            query |= Q(name=name)
        if id:
            query |= Q(id=id)

        data = list(User.objects.filter(query).values()[0:1])
        response_data = {
            'data': data,
            'success': True,
            'msg': '成功',
            'code': 200
        }
    else:
        response_data = {
            'data': [],
            'success': False,
            'msg': '失败',
            'code': 500
        }
    return JsonResponse(response_data, safe=False)
# 根据id修改


def update(req):
    if req.method == 'GET':
        id = req.GET.get('id')
        name = req.GET.get('name')
    else:
        id = None
        name = None
    if id and name:
        data = User.objects.get(id=id)
        data.name = name
        data.save()
        return JsonResponse({
            'data': list(User.objects.filter(id=id).values()),
            'success': True,
        }, safe=False)
    else:
        return JsonResponse({
            'data': [],
            'success': False,
            'msg': '失败',
            'code': 500
        }, safe=False)


# 根据id删除

def delete(req):
    id = req.GET.get('id')
    if id:
        User.objects.filter(id=id).delete()

        return JsonResponse({
            'data': [],
            'success': True,
            'msg': '成功',
        }, safe=False)
    else:
        return JsonResponse({
            'success': False,
            'msg': '失败,请传入id',
        }, safe=False)

# post请求参数json格式


@csrf_exempt  # 解决post请求403问题
def postJson(req):
    content_type = req.content_type.lower()
    # 根据请求类型返回不同的数据
    obj = {}
    obj['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    if content_type == 'application/json':
        data = json.loads(req.body)
        obj['name'] = data.get('name')
    else:  # application/x-www-form-urlencoded multipart/form-data
        obj['name'] = req.POST.get('name')
    return JsonResponse(obj, safe=False)
