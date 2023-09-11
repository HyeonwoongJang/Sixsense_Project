from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin

# UserModel(사용자 모델)을 관리자 인터페이스에서 관리해줍니다.
admin.site.register(User, UserAdmin)

# @admin.register(User) 
class UserAdmin(admin.ModelAdmin):
  list_display = ["id", "username", "email", "nickname", "created_at", "updated_at"]