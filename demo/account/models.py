from django.db import models
from pickle import TRUE
from utils.basemodels import BaseModel
# Create your models here.

class User(BaseModel):
    id = models.AutoField(primary_key=True)
    username = models.CharField('用户名', max_length=32, null = True, blank = True, unique = True)
    password = models.CharField('密码', max_length=32)
    email = models.EmailField('邮箱', null=True, blank=True, unique=True)
    
    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        
