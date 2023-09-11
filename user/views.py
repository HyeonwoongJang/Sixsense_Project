from django.http import HttpResponse
from django.shortcuts import render

from user.models import User

def signup(request):
  if request.method == 'GET':
    return render(request, 'user/signup.html')
  elif request.method == 'POST':
      username = request.POST['username'],
      password = request.POST['password'],
      password2 = request.POST['password2'],
      email = request.POST['email']
      image = request.POST['image']
      nickname = request.POST['nickname']
      if password == password2 :
        User.objects.create_user(username=username, password=password, password2=password2, email=email, image=image, nickname=nickname)
      else :
        return HttpResponse('password does not match')
  else:
    return HttpResponse("Invalid request method", status=405)
