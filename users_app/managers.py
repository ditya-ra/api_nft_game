from django.apps import apps
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, telegram_id, password):
        if not telegram_id:
            raise ValueError('Telegram ID must be set')

        user = self.model(telegram_id=telegram_id)
        user.set_password(password)
        user.save(using=self._db)

        advanced_user_model = apps.get_model('users_app', "AdvancedUser")
        advanced_user = advanced_user_model(user=user)
        advanced_user.save()

        return user

    def create_superuser(self, telegram_id, password):
        user = self.create_user(
            telegram_id=telegram_id,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
