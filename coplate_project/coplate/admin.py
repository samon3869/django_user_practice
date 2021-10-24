from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Review
# Register your models here.

admin.site.register(User, UserAdmin)
# custom fields 라는 섹션 아래에 nicknmae field를 추가!
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname",)}),)

admin.site.register(Review)