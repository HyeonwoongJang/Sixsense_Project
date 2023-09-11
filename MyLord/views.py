from django.shortcuts import render
from post.models import Post
from django.http import HttpResponse


def main(request):
    if request.method == 'GET':
        all_Post = Post.objects.all().order_by('-created_at')
        context = {"tem_all_Post": all_Post}
        return render(request, 'main.html', context)
    else:
        return HttpResponse("invalid request method", status=405)