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