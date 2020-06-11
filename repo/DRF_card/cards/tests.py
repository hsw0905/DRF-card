from cards.models import Cards
from munch import Munch
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker
from users.models import Users

class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.cards = baker.make('cards.Cards', _quantity=3)
        self.users = baker.make('users.Users', _quantity=3)

    def test_should_list(self):
        card = self.cards[0]
        self.client.force_authenticate(user = card.owner)

        response = self.client.get('/api/cards/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for card_response, card in zip(response.data['results'], self.cards[::-1]):
            self.assertEqual(card_response['id'], card.id)
            self.assertEqual(card_response['owner'], card.owner)

    def test_should_create(self):
        card = self.cards[0]
        user = self.users[0]
        data = {"title":"abc",
                "owner":f"{user.user_name}"}
        self.client.force_authenticate(user=card.owner)

        response = self.client.post('/api/users/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        card_response = Munch(response.data)
        self.assertTrue(card_response.id)
        self.assertEqual(card_response.owner, data['owner'])
