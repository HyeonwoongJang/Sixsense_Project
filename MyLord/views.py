from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.shortcuts import redirect, render
from post.models import Post
from django.http import HttpResponse
from user.models import User


def main(request):
    if request.method == 'GET':
        all_post = Post.objects.all().order_by('-created_at')
        context = {"tem_all_post": all_post}
        return render(request, 'main.html', context)
    else:
        return HttpResponse("invalid request method", status=405)


def myhome(request, user_id):
    if request.method == "GET":
        my_posts = Post.objects.filter(username_id=user_id).order_by('-created_at')
        return render(request, 'myhome.html', {'tem_my_posts': my_posts})
    else:
        return HttpResponse("invalid request method", status=405)


def profile(request, user_id):
    if request.method == "GET":
        my_info = User.objects.get(id=user_id)
        return render(request, 'profile.html', {'tem_my_info': my_info})
    elif request.method == "POST":
        edit_info = User.objects.get(id=user_id)
        edit_info.email = request.POST['email']
        edit_info.image = request.FILES.get('image')
        edit_info.nickname = request.POST['nickname']
        edit_info.save()
        return redirect(f'/profile/{edit_info.id}/')
    else:
        return HttpResponse("invalid request method", status=405)


def password(request, user_id):
    if request.method == "GET":
        my_password = User.objects.get(id=user_id)
        return render(request, 'password.html', {"tem_my_password": my_password})
    elif request.method == "POST":
        my_p = User.objects.get(id=user_id)
        if check_password(request.POST['password'], my_p.password):
            if request.POST['new_password'] == request.POST['new_password_check']:
                my_p.set_password(request.POST['new_password'])
                my_p.save()
                return redirect(f'/profile/{my_p.id}/')
            else:
                return HttpResponse("invalid request 222", status=405)
        else:
            return HttpResponse("invalid request 111", status=405)
    else:
        return HttpResponse("invalid request method", status=405)
