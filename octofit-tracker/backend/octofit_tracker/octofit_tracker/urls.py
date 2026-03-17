import os
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .views import (
    ActivityViewSet,
    LeaderboardViewSet,
    TeamViewSet,
    UserProfileViewSet,
    WorkoutViewSet,
    api_root,
)

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"


def codespace_api_root(request, *args, **kwargs):
    if codespace_name:
        request.META['HTTP_HOST'] = f"{codespace_name}-8000.app.github.dev"
        request.META['wsgi.url_scheme'] = 'https'
        request.META['HTTP_X_FORWARDED_PROTO'] = 'https'
    return api_root(request, *args, **kwargs)

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'activities', ActivityViewSet, basename='activities')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workouts')

urlpatterns = [
    path('', codespace_api_root, name='root-api'),
    path('admin/', admin.site.urls),
    path('api/', codespace_api_root, name='api-root'),
    # DefaultRouter publishes users/teams/activities/leaderboard/workouts endpoints.
    path('api/', include(router.urls)),
]
