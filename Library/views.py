from django.forms import model_to_dict
from django.shortcuts import render

import json
import time

from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .models import Book, Publish, Author, AuthorDetail
# Create your views here.


def init(request):
    """"
      insert into app01_publish(name,city,email) values ("华山出版社", "华山", "hs@163.com"), ("明教出版社", "黑木崖", "mj@163.com")
      # 先插入 authordetail 表中多数据
      insert into app01_authordetail(gender,tel,address,birthday) values (1,13432335433,"华山","1994-5-23"), (1,13943454554,"黑木崖","1961-8-13"), (0,13878934322,"黑木崖","1996-5-20")

      # 再将数据插入 author，这样 author 才能找到 authordetail
      insert into app01_author(name,age,au_detail_id) values ("令狐冲",25,1), ("任我行",58,2), ("任盈盈",23,3)
    """
    Publish.objects.create(name="华山出版社", city="华山", email="hs@163.com")
    Publish.objects.create(name="明教出版社", city="黑木崖", email="mj@163.com")

    AuthorDetail.objects.create(
        gender=1, tel=13432335433, address="华山", birthday="1994-5-23")

    AuthorDetail.objects.create(
        gender=1, tel=13943454554, address="黑木崖", birthday="1961-8-13")
    # 指定字段插入
    AuthorDetail.objects.create(
        gender=0, tel=13878934322, address="黑木崖", birthday="1996-5-20")

    Author.objects.create(name="令狐冲", age=25, email='123@312', au_detail_id=1)
    Author.objects.create(name="任我行", age=58, email='222@312', au_detail_id=2)
    Author.objects.create(name="任盈盈", age=23,
                          email='33333@312', au_detail_id=3)

    return JsonResponse({
        'data': '初始化成功',
        'success': True,
    })


def add_book(request):
    """"
    1. 通过对象关联的方式添加数据
    # 获取出版社对象
    publish_obj = Publish.objects.filter(name="华山出版社").first()
    # 给书籍的出版社属性publish传出版社对象
    book = Book.objects.create(title="天龙八部-21", price=100, pub_date="1986-07-24",
                               publish=publish_obj)
    """
    """
    2. 通过外键id添加数据
    # publish_obj = Publish.objects.filter(pk=2).first()
    # pk = publish_obj.pk
    # book = Book.objects.create(title="天龙八部-22", price=100, pub_date="1986-07-24",
    #                            publish_id=pk)
    """
    """
    3. 通过对象关联的方式添加数据
    chong = Author.objects.filter(name="令狐冲").first()
    ying = Author.objects.filter(name="任盈盈").first()
    book = Book.objects.filter(title="天龙八部-21").first()
    book.authors.add(chong, ying)
    chong_dict = model_to_dict(chong)
    ying_dict = model_to_dict(ying)
    book_dict = model_to_dict(book)
    book_dict['authors'] = [chong_dict, ying_dict]
    """
    """
    4. 通过外键id添加数据
    chong = Author.objects.filter(name="令狐冲").first()
    pk = chong.pk
    book = Book.objects.filter(title="天龙八部-22").first()
    book.authors.add(pk)
    book_dict = model_to_dict(book)
    book_dict['authors'] = [model_to_dict(chong)]
    """
    author = Author.objects.filter(name="令狐冲").first()
    book = Book.objects.create(title="西游记", price=100, pub_date="1986-07-24",
                               publish_id=1,)
    book.authors.add(author)

    book_dict = model_to_dict(book)
    book_dict['publish'] = model_to_dict(book.publish)
    book_dict['authors'] = [model_to_dict(author)]
    return JsonResponse({
        'data': book_dict,  # 返回新增的book
        'success': True,
    }, safe=False)


def getList(request):
    # 查询所有书籍 包含出版社信息 和 作者信息
    bookList = Book.objects.filter(title='西游记').all()
    dataLen = len(bookList)
    result = []
    for book in bookList:
        authors = []
        for i in book.authors.all():
            author_dict = {
                'name': i.name,
                'age': i.age,
                'email': i.email,
                'au_detail': model_to_dict(i.au_detail)
            }
            authors.append(author_dict)
        book_dict = {
            'id': book.id,
            'title': book.title,
            'price': book.price,
            'pub_date': book.pub_date,
            'publish': model_to_dict(book.publish),
            'authors': authors
        }
        result.append(book_dict)
    return JsonResponse({
        'data': result,
        'length': dataLen,
        'success': True,
    }, safe=False)


def findBy(request):

    pass


def update(request):

    pass


def delete(request):

    pass
