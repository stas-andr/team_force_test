from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin


class MyUserAdmin(admin.ModelAdmin):
    fields = ('last_name', 'first_name', 'middle_name',
              'email', 'is_active')


admin.site.register(MyUser, MyUserAdmin)
