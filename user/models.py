from django.db import models
from django.contrib.auth.models import AbstractUser


"""
username : 로그인 시 사용되는 사용자의 ID
password : 로그인 시 사용되는 사용자의 비밀번호
email : 사용자의 Email
img : 사용자의 프로필 사진
nickname : 사용자의 활동 이름
created_at : 사용자의 계정이 생성된 시간
updated_at : 사용자의 계정 정보가 수정된 시간
"""


class User(AbstractUser):
    image = models.ImageField(blank=True, null=True)
    nickname = models.CharField(max_length=20, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    follow = models.ManyToManyField('self', related_name="follower", symmetrical=False)

    
def __str__(self):
    return self.username