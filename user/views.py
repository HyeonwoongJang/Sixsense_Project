from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
        image = request.FILES.get("image")
        nickname = request.POST['nickname']
        if password == password2:
            User.objects.create_user(
                username=username, password=password, email=email, image=image, nickname=nickname)
            return redirect('/user/signin/')
        else:
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
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/signin.html')
    else:
        return HttpResponse("Invalid request method", status=405)


def signout(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")
    else:
        return HttpResponse("Invalid request method", status=405)


# follow = models.ManyToManyField('self', related_name="following", symmetrical=False)

# 팔로우를 누르면, 해당 유저의 user_id를 가져옴.
@login_required
def follow(request, user_id):
    if request.method == "POST" :
        user = User.objects.get(id=user_id)
        # print(dir(user))
        me = request.user
    # User 모델의 follow 필드는 User 모델을 참조, 사용자가 해당 사용자를 팔로우하고 있는지 여부를 해당 사용자의 모델 데이터에서 참조......
        # if user.following.filter(id=request.user.id):
        if me in user.follower.all():
            user.follower.remove(request.user)
        else:
            user.follower.add(request.user)
        return redirect(f'/myhome/{user_id}/')


# @login_required
# def user_follow(request, id):
#     me = request.user
#     click_user = User.objects.get(id=id)
#     if me in click_user.following.all():
#         click_user.following.remove(request.user)
#     else:
#         click_user.following.add(request.user)
#     return redirect(f'/myhome/{user_id}/')
