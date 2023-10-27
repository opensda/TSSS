from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test user",
            password="12345",
        )
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            place="турник",
            time="4:20:00",
            action="анжумания",
            reward="пресс качат",
            user=self.user,
        )

    def test_get_habits(self):
        url = reverse("habits:habits-list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
