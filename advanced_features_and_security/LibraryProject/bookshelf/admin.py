from django.contrib import admin
from users.models import CustomUser
from users.admin import CustomUserAdmin

admin.site.register(CustomUser, CustomUserAdmin)
