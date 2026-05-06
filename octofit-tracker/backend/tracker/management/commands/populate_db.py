from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tracker.models import Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # Create users
        user1 = User.objects.create_user(username='alice', email='alice@example.com', password='password123')
        user2 = User.objects.create_user(username='bob', email='bob@example.com', password='password123')
        user3 = User.objects.create_user(username='charlie', email='charlie@example.com', password='password123')

        # Create teams
        team1 = Team.objects.create(name='Fitness Warriors', created_by=user1)
        team1.members.add(user1, user2)

        team2 = Team.objects.create(name='Health Heroes', created_by=user3)
        team2.members.add(user3)

        # Create activities
        Activity.objects.create(user=user1, activity_type='run', duration=45, distance=5.0, calories=300, date=date.today())
        Activity.objects.create(user=user2, activity_type='walk', duration=30, distance=3.0, calories=150, date=date.today())
        Activity.objects.create(user=user3, activity_type='cycle', duration=60, distance=20.0, calories=500, date=date.today())

        # Create leaderboards
        Leaderboard.objects.create(user=user1, total_points=100, total_activities=1, total_duration=45)
        Leaderboard.objects.create(user=user2, total_points=50, total_activities=1, total_duration=30)
        Leaderboard.objects.create(user=user3, total_points=200, total_activities=1, total_duration=60)

        # Create workouts
        Workout.objects.create(
            name='Morning Run',
            description='A simple morning run workout',
            exercises={'warmup': '5 min jog', 'main': '30 min run', 'cooldown': '5 min walk'},
            created_by=user1,
            is_public=True
        )

        Workout.objects.create(
            name='Strength Training',
            description='Full body strength workout',
            exercises={'squats': '3 sets of 10', 'pushups': '3 sets of 15', 'planks': '3 sets of 30s'},
            created_by=user2,
            is_public=False
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data'))