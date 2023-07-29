from django.contrib import admin
from user.models import Login
from user.models import Signup

# Register your models here.
admin.site.register(Login)
admin.site.register(Signup)