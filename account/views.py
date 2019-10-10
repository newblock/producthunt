from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        uname = request.POST['用户名']
        password = request.POST['密码']
        vpassword = request.POST['确认密码']
        try:
            User.objects.get(username=uname)
            return render(request, 'signup.html',{'用户名已存在':'该用户名已经存在'})

        except User.DoesNotExist:
            if password == vpassword:
                User.objects.create_user(username=uname,password=password)
                return redirect('主页')
            else:
                return render(request, 'signup.html', {'密码不一致': '密码不一致'})

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        pass_word = request.POST['密码']
        user = auth.authenticate(username=user_name,password=pass_word)
        if user is None:
            return render(request,'login.html',{'登陆出错':'用户名或密码错误'})
        else:
            auth.login(request,user)
            return redirect('主页')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('主页')