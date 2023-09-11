from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required(login_url='/user/signin/')
def create(request):
    if request.method == "GET":
        return render(request, "post/create.html")
    elif request.method == "POST":
        print(request.FILES.get("image"))
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
        post_detail = Post.objects.get(id=post_id)
        return render(request, 'post/detail.html', {'tem_post_detail': post_detail})
    
def delete(request, post_id):
    if request.method == "POST":
        post_delete=Post.objects.get(id=post_id)
        if request.user == post_delete.username:
            post_delete.delete()
            return redirect('/')
        else:
            return HttpResponse("invalid request method", status=403)
    else:
        return HttpResponse("Invalid request method", status=405)