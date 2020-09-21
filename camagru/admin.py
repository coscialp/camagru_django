from django.contrib import admin
from .models import User, Picture, Like, Dislike, Comment
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'last_name', 'first_name')


admin.site.register(User, UserAdmin)
admin.site.register(Picture)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Comment)

