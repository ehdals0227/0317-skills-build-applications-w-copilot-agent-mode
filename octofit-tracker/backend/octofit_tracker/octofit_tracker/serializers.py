from bson import ObjectId
from rest_framework import serializers

from .models import Activity, Leaderboard, Team, UserProfile, Workout


def _normalize_object_id(value):
    if isinstance(value, ObjectId):
        return str(value)
    if isinstance(value, dict):
        return {k: _normalize_object_id(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_normalize_object_id(v) for v in value]
    return value


class ObjectIdModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return _normalize_object_id(data)


class UserProfileSerializer(ObjectIdModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        read_only_fields = ["id"]


class TeamSerializer(ObjectIdModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
        read_only_fields = ["id"]


class ActivitySerializer(ObjectIdModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"
        read_only_fields = ["id", "recorded_at"]


class LeaderboardSerializer(ObjectIdModelSerializer):
    class Meta:
        model = Leaderboard
        fields = "__all__"
        read_only_fields = ["id"]


class WorkoutSerializer(ObjectIdModelSerializer):
    class Meta:
        model = Workout
        fields = "__all__"
        read_only_fields = ["id"]
