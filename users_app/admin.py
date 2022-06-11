from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserAdminChangeForm
from .models import AdvancedUser

User = get_user_model()

admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm

    list_display = ['telegram_id', 'is_active', 'admin', 'staff']
    list_filter = ['admin']

    ordering = ['telegram_id']
    filter_horizontal = ()


class AdvancedUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'level', 'productivity', 'balance', 'nft']


admin.site.register(User, UserAdmin)
admin.site.register(AdvancedUser, AdvancedUserAdmin)
