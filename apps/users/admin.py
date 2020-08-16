from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


# Register your models here.
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile_number', 'username', 'email', 'is_active')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined')
