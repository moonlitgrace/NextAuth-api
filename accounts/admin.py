from django.contrib import admin

from .models import CustomUser, Feedback


class AdminUser(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_superuser', 'is_staff']
admin.site.register(CustomUser, AdminUser)

admin.site.register(Feedback)