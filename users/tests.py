from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """ Тестирование модели Habits """

    def setUp(self):
        """ Создание тестовой модели Пользователя"""

        self.user = User.objects.create(
            email="test@test.com",
            password="testpassword",
            tg_chat_id='1567728836'
        )

        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """ Тестирование создания пользователя """

        url = reverse("users:register")
        data = {
            "email": "test2@test.com",
            "password": "testpassword",
            "tg_chat_id": "1567728836",
            "is_superuser": "False"
        }

        response = self.client.post(url, data=data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("email"), "test2@test.com")
        self.assertEqual(data.get("tg_chat_id"), "1567728836")
        self.assertEqual(data.get("is_superuser"), False)

    def test_create_user_no_tg_chat_id(self):
        """ Тестирование создания пользователя """

        url = reverse("users:register")
        data = {
            "email": "test2@test.com",
            "password": "testpassword",
            "is_superuser": "False"
        }

        response = self.client.post(url, data=data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_user(self):
        """ Тестирование вывода всех пользователей """

        response = self.client.get(reverse('users:users_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()



        date_joined_text = str(self.user.date_joined)
        date_joined = date_joined_text[0:10] + 'T' + date_joined_text[11:26] + 'Z'


        result = [{
            "email": self.user.email,
            "first_name": "",
            "last_name": "",
            "tg_nick": None,
            "tg_chat_id": self.user.tg_chat_id,
            "last_login": None,
            "avatar": None,
            "date_joined": date_joined,
            "is_superuser": False,
            "is_staff": False,
            "is_active": True
        }]


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_user_retrieve(self):
        """ Тестирование просмотра одного пользователя """

        url = reverse("users:users_retrieve_update", args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("email"), "test@test.com")
        self.assertEqual(data.get("password"), "testpassword")
        self.assertEqual(data.get("tg_chat_id"), "1567728836")
        self.assertEqual(data.get("is_superuser"), False)

    def test_user_update(self):
        """Тестирование обновления пользователя"""
        url = reverse("users:users_retrieve_update", args=(self.user.pk,))
        data = {"tg_chat_id": "0000000000"}
        response = self.client.patch(url, data)

        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('tg_chat_id'), "0000000000")