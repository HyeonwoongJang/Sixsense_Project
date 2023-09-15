from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Comment, Like
from user.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required(login_url='/user/signin/')
def create(request):
    if request.method == "GET":
        return render(request, "post/create.html")
    elif request.method == "POST":
        Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            image=request.FILES.get("image"),
            username=request.user
        )
        return redirect('/')
    else:
        return HttpResponse("invalid request method", status=405)


def read(request, post_id):
    if request.method == 'GET':
        post_detail = Post.objects.get(id=post_id)  # 특정 포스트 들어갈 때
        comments = Comment.objects.filter(post_id=post_id).order_by(
            '-created_at')  # 특정 포스트의 해당 코멘트들 (Comment 테이블의 post_id 필드에 받아온 인자  )
        # 좋아요 조건문
        like_user = Like.objects.filter(post=post_id, user=request.user.id)
        # 북마크 조건문
        me = request.user
        click_user = Post.objects.get(id=post_id)
        if me in click_user.book_mark.all():
            bookmark_user = True
        else:
            bookmark_user = False
        return render(request, 'post/detail.html', {'tem_post_detail': post_detail, 'tem_comments': comments, 'tem_likes': like_user, 'tem_bookmark_user': bookmark_user})
    else:
        return HttpResponse("Invalid request method", status=405)


def delete(request, post_id):
    if request.method == "POST":
        post_delete = Post.objects.get(id=post_id)
        if request.user == post_delete.username:
            post_delete.delete()
            return redirect('/')
        else:
            return HttpResponse("invalid request method", status=403)
    else:
        return HttpResponse("Invalid request method", status=405)


def update(request, post_id):
    if request.method == "POST":
        post_update = Post.objects.get(id=post_id)
        if request.user == post_update.username:
            post_update.title = request.POST['title']
            post_update.content = request.POST['content']
            if request.FILES.get('image') is None:
                post_update.image = post_update.image
            else:
                post_update.image = request.FILES.get("image")
            post_update.save()
            return redirect(f"/post/{post_update.id}/")
        else:
            return HttpResponse("invalid request method", status=403)
    elif request.method == "GET":
        post_update = Post.objects.get(id=post_id)
        return render(request, 'post/update.html', {'tem_post_update': post_update})
    else:
        return HttpResponse("Invalid request method", status=405)


@login_required(login_url='/user/signin/')
def comment(request, post_id):
    if request.method == 'POST':
        pp = Post.objects.get(id=post_id)
        Comment.objects.create(
            content=request.POST['content'],
            post=pp,
            user=request.user
        )

        return redirect(f"/post/{post_id}/")
    else:
        return HttpResponse("invalid request method", status=405)


def comment_delete(request, comment_id):
    if request.method == "POST":
        comment_delete = Comment.objects.get(id=comment_id)
        if request.user.id == comment_delete.user.id:
            comment_delete.delete()
            return redirect(f"/post/{comment_delete.post.id}/")
        else:
            return HttpResponse("invalid request method", status=405)
    else:
        return HttpResponse("invalid request method", status=405)

# dropdown박스로


@login_required
def like(request, post_id):
    if request.method == "POST":
        liked_post = Post.objects.get(id=post_id)
        like_user = Like.objects.filter(post=post_id, user=request.user.id)
        if like_user:
            like_user.delete()
        else:
            Like.objects.create(post=liked_post, user=request.user)
        return redirect(f'/post/{post_id}/')
    else:
        return HttpResponse("invalid request method", status=405)


# Like 테이블을 따로 선언하지 않고 ManyToManyField를 사용했을 경우,
# @login_required
# def like(request, post_id):
#     like_post = Post.objects.get(id=post_id)
#     if like_post.like_user.filter(id=request.user.id):
#         like_post.like_user.remove(request.user)
#     else:
#         like_post.like_user.add(request.user)
#     return redirect(f"/post/{post_id}/")

#   create > add ????
#   delete : 해당 데이터의 id........... remove : 삭제할 타겟 필드 설정 가능

@login_required
def bookmark(request, post_id):
    if request.method == "POST":
        book_post = Post.objects.get(id=post_id)

        # book_mark(필드) - User(모델) : ManyToMany 관계

        # # 특정 User가 북마크한 모든 포스트
        # user2 = User.objects.get(id=request.user.id)
        # posts_that_user2_bookmarked = user2.rn_book_mark.all()
        #

        # # 특정 Post를 북마크한 모든 사용자
        # post2 = Post.objects.get(id=2)
        # users_who_bookmarked_post2 = post2.rn_book_mark.all()
        #

        # Post 모델의 book_mark 필드는 User 모델을 참조, 조건식에서 book_mark는 User 인스턴스의 id를 역으로 참조
        if book_post.book_mark.filter(id=request.user.id):
            book_post.book_mark.remove(request.user)
        else:
            book_post.book_mark.add(request.user)
        return redirect(f"/post/{post_id}/")

# post1 = Post.objects.get(id=1)
# post1_likes = post1.rn_like_user.all()
# post1_user1_like = post1.rn_like_user.get(id=request.user.id)
