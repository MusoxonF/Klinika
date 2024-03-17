from django.db import models

from User.models import User, Bemor


class Tashxis(models.Model):
    bemor = models.ForeignKey(Bemor, on_delete=models.SET_NULL, null=True)
    diagnoz = models.TextField(null=True, blank=True)
    tashxis = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    narx = models.PositiveIntegerField(default=0)
    tuladi = models.PositiveIntegerField(default=0)
    qoldi = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.tashxis}/{self.narx}'
