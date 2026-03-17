from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Activity, Leaderboard, Team, UserProfile, Workout
from .serializers import (
    ActivitySerializer,
    LeaderboardSerializer,
    TeamSerializer,
    UserProfileSerializer,
    WorkoutSerializer,
)


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("users-list", request=request, format=format),
            "teams": reverse("teams-list", request=request, format=format),
            "activities": reverse("activities-list", request=request, format=format),
            "leaderboard": reverse("leaderboard-list", request=request, format=format),
            "workouts": reverse("workouts-list", request=request, format=format),
        }
    )


class UserProfileViewSet(viewsets.ModelViewSet):
    """CRUD endpoint for users collection."""

    queryset = UserProfile.objects.all().order_by("id")
    serializer_class = UserProfileSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """CRUD endpoint for teams collection."""

    queryset = Team.objects.all().order_by("id")
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """CRUD endpoint for activities collection."""

    queryset = Activity.objects.all().order_by("id")
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    """CRUD endpoint for leaderboard collection."""

    queryset = Leaderboard.objects.all().order_by("id")
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """CRUD endpoint for workouts collection."""

    queryset = Workout.objects.all().order_by("id")
    serializer_class = WorkoutSerializer
