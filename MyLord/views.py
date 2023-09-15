from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect, render
from post.models import Post, Comment, Like
from django.http import HttpResponse
from user.models import User
from django.contrib.auth import login


def main(request):
    if request.method == 'GET':
        all_post = Post.objects.all().order_by('-created_at')
        context = {"tem_all_post": all_post}
        return render(request, 'main.html', context)
    else:
        return HttpResponse("invalid request method", status=405)


def myhome(request, user_id):
    if request.method == "GET":
        page_user = User.objects.get(id=user_id)
        my_posts = Post.objects.filter(
            username_id=user_id).order_by('-created_at')
        follow = request.user in page_user.follower.all()
        me = request.user
        my_book_marks = me.rn_book_mark.all()
        my_like_posts = Like.objects.filter(user=request.user)
        return render(request, 'myhome.html', {'tem_my_posts': my_posts, 'tem_page_user': page_user, 'tem_follow': follow, 'tem_my_bookmarks': my_book_marks, 'tem_my_like_posts': my_like_posts})
    else:
        return HttpResponse("invalid request method", status=405)


def profile(request, user_id):
    if request.method == "GET":
        my_info = User.objects.get(id=user_id)
        return render(request, 'profile.html', {'tem_my_info': my_info})
    elif request.method == "POST":
        edit_info = User.objects.get(id=user_id)
        edit_info.email = request.POST['email']
        if request.FILES.get('image') is None:
            edit_info.image = edit_info.image
        else:
            edit_info.image = request.FILES.get("image")
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
                login(request, my_p)
                return redirect(f'/profile/{my_p.id}/')
            else:
                return HttpResponse("invalid request 222", status=405)
        else:
            return HttpResponse("invalid request 111", status=405)
    else:
        return HttpResponse("invalid request method", status=405)


def neighbor(request, user_id):
    if request.method == "GET":
        me = User.objects.get(id=user_id)
        followings = me.follow.all()
        followers = me.follower.all()

        return render(request, 'neighbors_list.html', {'tem_followings': followings, 'tem_followers': followers, 'tem_me': me, })
        # if me.follow.from_user_id :
        #     neighbors = User.objects.filter(user_follow_from_user_id=request.user.id)
        #     return render(request, 'neighbors_list.html', {'tem_neighbors':neighbors, 'tem_me':me})
        # else:
        #     return HttpResponse("invalid request method", status=405)
    else:
        return HttpResponse("invalid request method", status=405)

# def marks(request, user_id):
