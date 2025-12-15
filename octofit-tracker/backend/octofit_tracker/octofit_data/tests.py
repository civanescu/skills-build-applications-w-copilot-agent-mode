from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Team, Activity, Workout, Leaderboard
from django.contrib.auth import get_user_model

User = get_user_model()

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.activity = Activity.objects.create(name='Test Activity', description='Test Desc')
        self.workout = Workout.objects.create(name='Test Workout', reps=10)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=50)

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)

    def test_team_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)

    def test_activity_list(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)

    def test_workout_list(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_list(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)
