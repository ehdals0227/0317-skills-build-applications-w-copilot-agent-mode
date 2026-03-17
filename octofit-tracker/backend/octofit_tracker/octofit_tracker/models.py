from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hero_alias = models.CharField(max_length=100)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.name} ({self.hero_alias})"


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    universe = models.CharField(max_length=20)

    class Meta:
        db_table = "teams"

    def __str__(self):
        return self.name


class Activity(models.Model):
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "activities"

    def __str__(self):
        return f"{self.user_email} - {self.activity_type}"


class Leaderboard(models.Model):
    user_email = models.EmailField()
    points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "leaderboard"

    def __str__(self):
        return f"{self.user_email} ({self.points})"


class Workout(models.Model):
    user_email = models.EmailField()
    workout_name = models.CharField(max_length=100)
    intensity = models.CharField(max_length=20)
    duration_minutes = models.PositiveIntegerField()

    class Meta:
        db_table = "workouts"

    def __str__(self):
        return f"{self.user_email} - {self.workout_name}"
