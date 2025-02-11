from django.urls import path, re_path
# from app01.views import helloworld, article_create, article_detail, phone_number
from . import views


urlpatterns = [
    path('create/', views.article_create, name='article_create'),
    path('<int:article_id>/<str:title>/', views.article_detail, name='article_detail'),
    re_path('^phone/(?P<phone_number>1[3456789]\d{9})/$', views.phone_number, name='phone_number'),
    path('list/', views.list, name='article_list')
]