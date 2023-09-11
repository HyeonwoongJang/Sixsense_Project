from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from user.models import User


def signup(request):
  # 회원가입 페이지 함수 입니다.
  if request.method == 'GET':
    return render(request, 'user/signup.html')
  elif request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      password2 = request.POST['password2']
      email = request.POST['email']
      image=request.FILES.get("image")
      nickname = request.POST['nickname']
      if password == password2 :
        User.objects.create_user(username=username, password=password, email=email, image=image, nickname=nickname)
        return redirect('/user/signin/')
      else :
        return HttpResponse('password does not match')
  else:
    return HttpResponse("Invalid request method", status=405)

def signin(request):
    # 로그인 페이지 함수 입니다.
    if request.method == "GET":
        return render(request, 'user/signin.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/main/')
        else:
            return render(request, 'user/signin.html')
    else:
        return HttpResponse("Invalid request method", status=405)
