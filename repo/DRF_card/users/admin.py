from django.contrib import admin
from users.models import Users
from cards.models import Cards

# Register your models here.
admin.register(Users)
admin.register(Cards)