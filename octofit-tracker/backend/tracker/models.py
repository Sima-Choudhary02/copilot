from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('run', 'Run'),
        ('walk', 'Walk'),
        ('cycle', 'Cycle'),
        ('swim', 'Swim'),
        ('workout', 'Workout'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    distance = models.FloatField(null=True, blank=True, help_text='Distance in km')
    calories = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.activity_type} on {self.date}'

class Leaderboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_points = models.PositiveIntegerField(default=0)
    total_activities = models.PositiveIntegerField(default=0)
    total_duration = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.total_points} points'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    exercises = models.JSONField(help_text='List of exercises with sets, reps, etc.')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
