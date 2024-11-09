from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
 
from user.models import User
 
admin.site.register(User, UserAdmin)

admin.site.site_title = "DP 0.1.0v"
admin.site.site_header = "DP 0.1.0v"