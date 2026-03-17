from django.test import TestCase
from rest_framework.test import APIClient

from .models import Activity, Leaderboard, Team, UserProfile, Workout


class OctofitApiCollectionTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserProfile.objects.create(
            name="Peter Parker",
            email="spiderman@octofit.dev",
            hero_alias="Spider-Man",
        )
        Team.objects.create(name="marvel team", universe="Marvel")
        Activity.objects.create(
            user_email="spiderman@octofit.dev",
            activity_type="Wall Climb Sprint",
            duration_minutes=45,
            calories_burned=520,
        )
        Leaderboard.objects.create(
            user_email="spiderman@octofit.dev",
            points=820,
            rank=1,
        )
        Workout.objects.create(
            user_email="spiderman@octofit.dev",
            workout_name="Spider Core Blast",
            intensity="high",
            duration_minutes=40,
        )

    def setUp(self):
        self.client = APIClient()

    def test_api_root_contains_all_collection_links(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("users", response.data)
        self.assertIn("teams", response.data)
        self.assertIn("activities", response.data)
        self.assertIn("leaderboard", response.data)
        self.assertIn("workouts", response.data)

    def test_users_collection_endpoint(self):
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_teams_collection_endpoint(self):
        response = self.client.get("/api/teams/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_activities_collection_endpoint(self):
        response = self.client.get("/api/activities/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_leaderboard_collection_endpoint(self):
        response = self.client.get("/api/leaderboard/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_workouts_collection_endpoint(self):
        response = self.client.get("/api/workouts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
