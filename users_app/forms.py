from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdminChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['telegram_id', 'password', 'is_active', 'admin', 'staff']
