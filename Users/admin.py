from django.contrib import admin
from .models import User,Profile,UserManger
# Register your models here.
admin.site.register(User)
# admin.site.register(UserManger)
admin.site.register(Profile)