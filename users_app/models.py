from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from nft_shop_app.models import Nft
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    email = None
    telegram_id = models.IntegerField(unique=True, verbose_name='Идентификатор телеграмм')
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'telegram_id'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.telegram_id)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label=None):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin


class AdvancedUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    level = models.IntegerField(default=1, verbose_name='Уроверь персонажа')
    productivity = models.IntegerField(default=0, verbose_name="Продуктивность персонажа")
    balance = models.IntegerField(default=0, verbose_name='Баланс аккаунта')
    nft = models.ForeignKey(Nft, on_delete=models.PROTECT, blank=True, null=True)
