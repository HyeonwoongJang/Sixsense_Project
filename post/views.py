from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required


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
