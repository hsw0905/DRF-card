from django.db import models

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=15)
    user_password = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=50, default="test@example.com")
    user_cards_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['updated']