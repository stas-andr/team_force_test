from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import MyUser, Profile, Tag

admin.site.register(MyUser, UserAdmin)
admin.site.register(Profile)
admin.site.register(Tag)
