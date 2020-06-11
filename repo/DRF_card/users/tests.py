from users.models import Users
from munch import Munch
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker

class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.users = baker.make('users.Users', _quantity=3)

    def test_should_list(self):
        user = self.users[0]
        self.client.force_authenticate(user=user)

        response = self.client.get('/api/users/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for user_response, user in zip(response.data['results'], self.users[::-1]):
            self.assertEqual(user_response['id'], user.id)
            self.assertEqual(user_response['user_name'], user.user_name)


    def test_should_create(self):
        data = {"user_name":"abc"}

        response = self.client.post('/api/users/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user_response = Munch(response.data)
        self.assertTrue(user_response.id)
        self.assertEqual(user_response.user_name, data['user_name'])

    def test_should_get(self):
        user = self.users[0]
        self.client.force_authenticate(user=user)

        response = self.client.get(f'/api/users/{user.id}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_response = Munch(response.data)
        self.assertTrue(user_response.id)
        self.assertEqual(user_response.user_name, user.user_name)

    def test_should_update(self):
        user = self.users[0]
        prev_username = user.user_name
        self.client.force_authenticate(user=user)
        data = {'user_name':'new',
                'user_password':'1111',}

        response = self.client.put(f'/api/users/{user.id}', data=data)

        user_response = Munch(response.data)
        print(user_response)
        self.assertTrue(user_response.id)
        self.assertNotEqual(user_response.user_name, prev_username)
        self.assertEqual(user_response.user_name, data['user_name'])

    def test_should_delete(self):
        user = self.users[0]
        self.client.force_authenticate(user=user)
        entry = Users.objects.get(id = user.id)

        response = self.client.delete(f'/api/users/{user.id}')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Users.objects.filter(id = entry.id).exists())

