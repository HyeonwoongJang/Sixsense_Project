from django.shortcuts import render
from post.models import Post
from django.http import HttpResponse


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