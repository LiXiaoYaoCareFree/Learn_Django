from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse("Hello World")


def article_create(request):
    return HttpResponse("article create")


def article_detail(request, article_id, title):
    return HttpResponse(f'文章的id是{article_id}, 标题是{title}')

def phone_number(request, phone_number):
    return HttpResponse(f'手机号码是{phone_number}')


def list(request):
    author = 'andy'
    article_number = 20
    article_list = [
        '第一篇文章: 什么是Django',
        '第二篇文章: Django的MTV',
        '第三篇文章: Django的请求与响应',
    ]
    info = {
        'name': author,
        'age': 18,
        'programming_language': ['python', 'java', 'c++'],
    }
    content = """

    """
    return render(request, 'list.html', {
        'author': author,
        'number': article_number,
        'article_list': article_list,
        'info': info,
        'content': content,
    })