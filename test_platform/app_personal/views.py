from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
# 用来写请求的处理逻辑

def hello(request):
    return render(request, 'hello.html')


def login(request):
    """
    用户登录
    """
    #返回登录页面
    if request.method == 'GET':
        return render(request, 'login.html', {'error': '登录页面'})

    #处理登录请求
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if username == '' or password == '':
            return render(request, 'login.html', {
                'error': '用户名或密码为空!'
            })

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) #记录用户的登录状态
            response = HttpResponseRedirect('/manage/')
            response.set_cookie('user', username, 3600)
            return response
        else:
            return render(request, 'login.html', {
                'error': '用户名或密码错误!'
            })





@login_required
def logout(requset):
    """
    退出登录
    """
    auth.logout(requset)
    return HttpResponseRedirect('/') #退出后重定向到首页


