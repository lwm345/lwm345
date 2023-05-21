from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
#
# def login(request):
#   return HttpResponse("登录页面")


from django.shortcuts import render, redirect


def login(request):
    # print("==========")
    if request.method == 'POST':
        # print("==============================================")
        username = request.POST.get('username')
        passowrd = request.POST.get('password')
        print(username,passowrd)
        if username == 'root' and passowrd == '123456':
            return redirect('/')
        else:
            return render(request, 'login.html', {"error": "用户名或密码错误"})
    if request.method=='GET':
        return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')
