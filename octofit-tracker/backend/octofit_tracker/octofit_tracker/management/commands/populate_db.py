from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, Leaderboard, Team, UserProfile, Workout


class Command(BaseCommand):
    help = "octofit_db 데이터베이스에 테스트 데이터를 입력합니다."

    def handle(self, *args, **options):
        # Clear existing data with ORM before loading fixtures.
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        UserProfile.objects.all().delete()

        Team.objects.bulk_create(
            [
                Team(name="marvel team", universe="Marvel"),
                Team(name="dc team", universe="DC"),
            ]
        )

        users = [
            UserProfile(name="Peter Parker", hero_alias="Spider-Man", email="spiderman@octofit.dev"),
            UserProfile(name="Tony Stark", hero_alias="Iron Man", email="ironman@octofit.dev"),
            UserProfile(name="Bruce Wayne", hero_alias="Batman", email="batman@octofit.dev"),
            UserProfile(name="Clark Kent", hero_alias="Superman", email="superman@octofit.dev"),
        ]
        UserProfile.objects.bulk_create(users)

        Activity.objects.bulk_create(
            [
                Activity(
                    user_email="spiderman@octofit.dev",
                    activity_type="Wall Climb Sprint",
                    duration_minutes=45,
                    calories_burned=520,
                ),
                Activity(
                    user_email="ironman@octofit.dev",
                    activity_type="Flight Intervals",
                    duration_minutes=35,
                    calories_burned=480,
                ),
                Activity(
                    user_email="batman@octofit.dev",
                    activity_type="Night Rooftop Run",
                    duration_minutes=60,
                    calories_burned=610,
                ),
                Activity(
                    user_email="superman@octofit.dev",
                    activity_type="Hypersonic Cardio",
                    duration_minutes=30,
                    calories_burned=700,
                ),
            ]
        )

        Leaderboard.objects.bulk_create(
            [
                Leaderboard(user_email="superman@octofit.dev", points=980, rank=1),
                Leaderboard(user_email="batman@octofit.dev", points=910, rank=2),
                Leaderboard(user_email="ironman@octofit.dev", points=870, rank=3),
                Leaderboard(user_email="spiderman@octofit.dev", points=820, rank=4),
            ]
        )

        Workout.objects.bulk_create(
            [
                Workout(
                    user_email="spiderman@octofit.dev",
                    workout_name="Spider Core Blast",
                    intensity="high",
                    duration_minutes=40,
                ),
                Workout(
                    user_email="ironman@octofit.dev",
                    workout_name="Arc Reactor Circuit",
                    intensity="medium",
                    duration_minutes=50,
                ),
                Workout(
                    user_email="batman@octofit.dev",
                    workout_name="Gotham Strength Block",
                    intensity="high",
                    duration_minutes=55,
                ),
                Workout(
                    user_email="superman@octofit.dev",
                    workout_name="Kryptonian Endurance",
                    intensity="high",
                    duration_minutes=45,
                ),
            ]
        )

        self.stdout.write(self.style.SUCCESS("테스트 데이터 적재 완료"))
