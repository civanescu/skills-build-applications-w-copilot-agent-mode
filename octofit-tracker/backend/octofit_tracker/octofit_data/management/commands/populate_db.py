from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction
from django.apps import apps

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        Team = apps.get_model('octofit_data', 'Team', require_ready=False) if apps.is_installed('octofit_data') else None
        Activity = apps.get_model('octofit_data', 'Activity', require_ready=False) if apps.is_installed('octofit_data') else None
        Leaderboard = apps.get_model('octofit_data', 'Leaderboard', require_ready=False) if apps.is_installed('octofit_data') else None
        Workout = apps.get_model('octofit_data', 'Workout', require_ready=False) if apps.is_installed('octofit_data') else None

        with transaction.atomic():
            User.objects.all().delete()
            if Team: Team.objects.all().delete()
            if Activity: Activity.objects.all().delete()
            if Leaderboard: Leaderboard.objects.all().delete()
            if Workout: Workout.objects.all().delete()

            marvel = Team.objects.create(name='Marvel') if Team else None
            dc = Team.objects.create(name='DC') if Team else None

            users = [
                {'username': 'ironman', 'email': 'ironman@marvel.com', 'team': marvel},
                {'username': 'captainamerica', 'email': 'cap@marvel.com', 'team': marvel},
                {'username': 'batman', 'email': 'batman@dc.com', 'team': dc},
                {'username': 'superman', 'email': 'superman@dc.com', 'team': dc},
            ]
            for u in users:
                user = User.objects.create_user(username=u['username'], email=u['email'], password='password123')
                if Team and u['team']:
                    user.team = u['team']
                    user.save()

            if Activity:
                Activity.objects.create(name='Running', description='Run 5km')
                Activity.objects.create(name='Swimming', description='Swim 1km')
            if Workout:
                Workout.objects.create(name='Pushups', reps=20)
                Workout.objects.create(name='Situps', reps=30)
            if Leaderboard:
                Leaderboard.objects.create(user=User.objects.first(), score=100)

        self.stdout.write(self.style.SUCCESS('Test data populated in octofit_db.'))
