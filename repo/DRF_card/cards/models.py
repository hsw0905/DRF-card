from django.db import models

# Create your models here.
from users.models import Users


class Cards(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    contents = models.TextField()
    owner = models.ForeignKey(Users, related_name='author', on_delete=models.CASCADE, null=True,)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['updated']