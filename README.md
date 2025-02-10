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

### 基于函数视图实现登录功能
views(视图):
一个视图可以称之为函数或者视图类, 本质上是一个python函数或者是类, 用于处理用户的请求并返回响应。
![views(视图)](views.jpg)
分为: FBV(基于函数的视图)和CBV(基于类的视图)

### 基于类的视图实现登录功能

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