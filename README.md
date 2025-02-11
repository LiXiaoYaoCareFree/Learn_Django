# Learning Django

## 配置git
```
ls ~/.ssh(查看是否有公钥和私钥)
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"(生成公钥和私钥)(在github上添加公钥)
ssh -T git@github.com(测试连接)
git init(初始化)
git config --global user.name "your name"(用户名要和github一致)
git config --global user.email "your email"(邮箱要和github一致)
git remote -v(查看远程仓库)
git remote add origin git@uername:username/repositoryname.git(添加远程仓库)
git push -u origin master(第一次推送)
git add .(添加所有文件)
git commit -m "your message"(提交)
```

## 虚拟环境下安装django
```
python -m venv venv
# 创建虚拟环境
venv\Scripts\activate
# 激活虚拟环境
pip list
# 查看虚拟环境下安装的包
pip install django
# 安装django
```

### 虚拟环境和系统全局Python的区别
每个 Python 项目 都应该使用虚拟环境，避免库冲突和版本问题。
| **是否激活 `venv`** | **Python 解释器** | **安装的库** | **适用场景** |
|----------------|-------------------|------------|------------|
| ✅ **激活** (`venv\Scripts\activate`) | **虚拟环境中的 Python** (`venv\Scripts\python.exe`) | 仅对当前项目有效 | **开发项目、运行代码、管理依赖** |
| ❌ **未激活** | **系统全局 Python** (`C:\Python39\python.exe`) | 影响整个系统 | 仅用于全局 Python 操作 |



## 创建django
```
django-admin startproject demo
# 创建django项目
python manage.py runserver
# 运行django

```

## django的MVT模式

```
MVT 是 Django 框架的核心架构：
Model 负责数据
View 负责逻辑
Template 负责页面展示
```

```
MVT 处理流程
1. 用户访问 URL，Django 的 urls.py 解析请求。
2. View 处理请求，查询 Model 获取数据。
3. 数据传递给 Template，通过 Django 模板语言渲染 HTML 页面。
4. 返回 HTML 响应，展示给用户。
```
![MVT模式](MVT模式.jpg)


## 创建应用
```
# 启动虚拟环境
venv\Scripts\activate
# 进入项目目录
cd demo
# 创建应用
django-admin startapp app
```

## 路由匹配模式
```
URL就是用户输入的网址
路由就是处理URL和视图函数的之间的调度器
路由匹配模式就是将URL和视图函数进行匹配的过程
路由匹配模式1: 字符串精确模式
路由匹配模式2: 路径转换器格式
路由匹配模式3: 正则表达式模式
路由匹配模式4: 路由嵌套模式
```



## Django框架视图和模板

### 1.基于函数视图实现登录功能
views(视图):
一个视图可以称之为函数或者视图类, 本质上是一个python函数或者是类, 用于处理用户的请求并返回响应。
![views(视图)](views.jpg)
分为: FBV(基于函数的视图)和CBV(基于类的视图)

### 2.基于类的视图实现登录功能


## HttpRequest请求对象
```
请求对象的主要内容：
1. 获取请求头
2. 获取请求参数
```
### 获取请求参数
1. 获取GET参数:
```
value = request.GET.get('parameter_name', default_value)
```
2. 获取POST参数:
```
value = request.POST.get('parameter_name', default_value)
```
3. 获取URL参数(例如在URL中使用的参数):
```
value = request.GET.get('parameter_name', default_value)
```
4. 获取请求体中的JSON参数:
```
data = json.loads(request.body)
value = data.get('parameter_name', default_value)
```
5. 获取路径参数(例如在URL路径中的参数):
```
def my_view(request, parameter_name):
# 使用parameter_name参数
```
6. 获取请求头中的参数:
```
value = request.headers.get('Header-Name', default_value)
```



### GET和POST的区别

`GET` 请求和 `POST` 请求是 HTTP 协议中的两种常见请求方法，它们的主要区别如下：  

|  区别点  | `GET` 请求 | `POST` 请求 |
|---------|----------|------------|
| **用途** | 主要用于获取数据，不会对服务器资源产生影响 | 主要用于提交数据，通常用于修改服务器上的资源 |
| **参数传递** | 参数拼接在 URL 中，形式如 `?key=value&key2=value2` | 参数放在请求体（body）中，通常以 JSON、表单等格式传输 |
| **可见性** | 参数直接暴露在 URL 中，容易被看到 | 参数在请求体中，不直接暴露在 URL |
| **安全性** | 安全性较低，数据可能被缓存、记录到浏览器历史中 | 相对更安全，数据不会出现在 URL 中 |
| **数据长度限制** | 受 URL 长度限制（不同浏览器和服务器限制不同，通常不超过 2000 字符） | 没有长度限制，适合传输大数据 |
| **是否可缓存** | 可以被浏览器或代理服务器缓存 | 默认不会被缓存 |
| **幂等性** | 幂等（同样的请求多次执行，结果相同） | 非幂等（多次执行可能导致服务器数据变化） |
| **书签支持** | 可以存为书签，方便访问 | 不能存为书签 |

---

### **示例：GET 请求**
```python
import requests

url = "https://api.example.com/data"
params = {"id": 123, "name": "LLY"}

response = requests.get(url, params=params)
print(response.text)
```
发送的请求 URL 可能是：
```
https://api.example.com/data?id=123&name=LLY
```

---

### **示例：POST 请求**
```python
import requests

url = "https://api.example.com/submit"
data = {"username": "LLY", "password": "123456"}

response = requests.post(url, json=data)  # 发送 JSON 数据
print(response.text)
```
请求的数据不会出现在 URL，而是在请求体中发送。

---

### **总结**
- **`GET` 适用于查询数据（如查询天气、获取用户信息）。**
- **`POST` 适用于提交数据（如登录、上传文件、提交表单）。**




## HttpResponse响应对象
```
1. HttpResponse
2. JsonResponse
```



## 模板引擎和配置(Template)
Django中的模板就是用来动态生成HTML页面的。
1. 模板引擎和配置
```
DTL, Jinja2
```
2. 模板中的变量
```
数字，字符串，列表，元组，字典，集合，对象
```
3. 模板标签
```
· 循环控制
· 条件控制
· 模板注释
· URL解析
· with语句块
· 时间显示
· 继承语包含
```
```
# 循环列表或元组
{% for item in my_list %}
<li>内容</li>
{% empty %}
<li>暂无内容</li>
{% endfor %}
```
4. 模板过滤器
```
基础语法:
{{ value | filter_name:params }}
常用的过滤器:
upper urlencode length default floatformat
safe random truncatechars
```
5. 模板继承和包含
```
# extends 继承
# include 包含
```




## Django框架模型
### 什么是ORM:
```
ORM(Object-Relational Mapping)就是对象关系映射
web开发就是在面向数据库编程
ORM就是将面向对象的编程和面向数据库的编程进行了映射
且不需要使用SQL语句进行数据库操作
```

DataBase                     面向对象

数据表                        类

数据行                        对象

表中的字段                    属性


## 配置mysql数据库
```
1. mysql -u root -p
# 输入密码

2. create database django_demo;
# 连接mysql

3. 安装mysql引擎
pip install pymysql


4. 打开demo\__init__.py文件
修改DATABASES配置
import pymysql
pymysql.install_as_MySQLdb()

5. 执行数据库迁移
# 生成迁移文件
python manage.py makemigrations
# 执行迁移
python manage.py migrate

# 修改settings.py文件配置数据库
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_demo',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '123456',
    }
}
```


## 创建模型
```
1. 安装应用
在settings.py中的INSTALLED_APPS下添加应用名
2. 模型文件
在app下创建models.py文件

在models.py文件中创建模型类
```


![字段类型(1).jpg](<字段类型 (1).jpg>)
![字段类型(2).jpg](<字段类型 (2).jpg>)

## 设置meta元数据

## ORM新增数据
```
# 方式1: sava()保存
python manage.py makemigrations
python manage.py migrate
python manage.py shell

from account.models import User
user_obj = User(username='admin', password='123456',email='admin@qq.com')
user_obj.save()

# 方式2: create()新增数据
user2 = User.objects.create(username='zhangsan',password='11111',email='zhangsan@qq.com')

# 方式3: bulk_create()批量新增数据
user3 = User(username='lisi',password='222222', email='lisi@qq.com')
user4 = User(username='wangwu',password='2223333', email='wangwu@qq.com')
user_list = [user3, user4]
User.objects.bulk_create(user_list)

# 方式4: 外键关联
from app01.models import Article
from datetime import datetime 
now = datetime.now()
user_obj.username
article1 = Article(id=1, title='第一篇文章',content='the first', publish_date=now,user=user_obj)
article1.save()


# create read update delete
```





## ORM查询数据
```
# 1. all(): 返回所有数据
user = User.objects.all()
user

for item in user:
    print(item.username)


# 2. get(**kwargs): 返回符合条件的一条数据
user = User.objects.get(username='zhangsan')
user
user.id, user.username, user.password, user.email

user = User.objects.get(pk=1)
user

user = User.objects.first()
user = User.objects.last()

User.objects.filter(id__gt=1)

# 3. filter(**kwargs): 返回符合条件的所有数据
```


## ORM查询条件
· 相等/等于/布尔条件
```
· gt: 大于某个值
· gte: 大于等于某个值
· lt: 小于某个值
· lte: 小于等于某个值
· isnull: 是否为null
```
```
User.objects.filter(id__lte=3)
User.objects.filter(username__isnull=True)
```
· 是否包含**字符串
```
· icontains: 不区分大小写
User.objects.filter(username__icontains='AN')
User.objects.filter(username__contains='an')
User.objects.filter(id__in=[2,4,6])

· contains: 包含**值
· in: 在**选项(列表)之内
```
· 以**开始/结束
· 日期及时间
· 外键关联




## ORM多条件查询
```
· 方式1: filter()指定多个条件
User.objects.filter(created_at__minute=44).filter(username__contains='an')

· 方式2: &运算符
User.objects.filter(created_at__minute=44)&User.objects.filter(username__contains='an')

· 方式3: Q()函数的使用，支持&(且) 和 | (或)
from django.db.models import Q
User.objects.filter(Q(created_at__minute=44)|Q(username__contains='an'))
```

## ORM更新数据
```
· 方式1: save()修改单条数据
user.save()
· 方式2: update()批量修改数据
user = User.objects.filter(id=2).update(password='2222',email='zhangsan@163.com')

user2 = User.objects.get(id=2)
Article.objects.filter(id=1).update(user=user2)
· 方式3: bulk_update()批量修改数据

```




