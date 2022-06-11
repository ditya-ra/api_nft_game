from django.db import models


class Nft(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    price = models.IntegerField()
    productivity = models.IntegerField()

    def __str__(self):
        return self.name
