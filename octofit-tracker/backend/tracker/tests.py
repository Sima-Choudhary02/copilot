from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class TeamModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.team = Team.objects.create(name='Test Team', created_by=self.user)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.created_by, self.user)

class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='run',
            duration=30,
            date='2023-01-01'
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'run')
        self.assertEqual(self.activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.leaderboard = Leaderboard.objects.create(user=self.user, total_points=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.total_points, 100)

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.workout = Workout.objects.create(
            name='Test Workout',
            created_by=self.user,
            exercises={'exercise1': '3 sets of 10'}
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Test Workout')
