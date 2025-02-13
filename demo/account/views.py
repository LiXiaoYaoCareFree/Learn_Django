from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        headers = {
            'token': '123456'
        }
        #return HttpResponse(f"用户名{username}密码{password}", 
        #        content_type="text/html;charset=utf-8",
        #        status=404, headers=headers)
        return JsonResponse({'code': 200, 'msg': '登录成功'})
    elif request.method == 'GET':
        print(request.META.get('REMOTE_ADDR'))
        print(request.headers.get('User-Agent'))
        return render(request, 'login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        return HttpResponse(f'用户名{username}密码{password}')