from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import MyUser, Profile, Tag


class MyUserAdmin(UserAdmin):
    list_display = ('last_name', 'first_name', 'middle_name',
                    'username', 'email')


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Profile)
admin.site.register(Tag)
