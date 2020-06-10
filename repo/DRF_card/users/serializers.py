from rest_framework import serializers
from .models import Users
from cards.serializers import CardsSerializer


class UsersSerializer(serializers.ModelSerializer):
    cards = CardsSerializer(source='cards_set', many=True)
    class Meta:
        model = Users
        fields = ['user_name',
                  'user_password',
                  'user_email',
                  'user_cards_count',
                  'cards',]