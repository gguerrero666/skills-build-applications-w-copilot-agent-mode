from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')
    def test_create_user(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@example.com', team=team, is_superhero=True)
        self.assertEqual(str(user), 'U')
    def test_create_activity(self):
        team = Team.objects.create(name='T2', description='d2')
        user = User.objects.create(name='U2', email='u2@example.com', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, type='run', duration=10, date='2025-01-01')
        self.assertIn('run', str(activity))
    def test_create_workout(self):
        workout = Workout.objects.create(name='W', description='desc')
        self.assertEqual(str(workout), 'W')
    def test_create_leaderboard(self):
        team = Team.objects.create(name='T3', description='d3')
        leaderboard = Leaderboard.objects.create(team=team, points=42)
        self.assertIn('T3', str(leaderboard))
