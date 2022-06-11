from django.db import models


class Job(models.Model):
    text = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.id)
