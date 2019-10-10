from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
                User.objects.create(username=uname,password=password)
                return redirect('主页')
            else:
                return render(request, 'signup.html', {'密码不一致': '密码不一致'})
