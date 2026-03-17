from django.contrib import admin

from .models import Activity, Leaderboard, Team, UserProfile, Workout


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "hero_alias")
    search_fields = ("name", "email", "hero_alias")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "universe")
    search_fields = ("name", "universe")


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("id", "user_email", "activity_type", "duration_minutes", "calories_burned")
    search_fields = ("user_email", "activity_type")


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ("id", "user_email", "points", "rank")
    search_fields = ("user_email",)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("id", "user_email", "workout_name", "intensity", "duration_minutes")
    search_fields = ("user_email", "workout_name", "intensity")
