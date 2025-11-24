from django.core.management.base import BaseCommand
from octofit_tracker import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        from datetime import date
        # Delete existing data
        models.Activity.objects.all().delete()
        models.Workout.objects.all().delete()
        models.User.objects.all().delete()
        models.Leaderboard.objects.all().delete()
        models.Team.objects.all().delete()

        # Create teams
        marvel = models.Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = models.Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        tony = models.User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel, is_superhero=True)
        steve = models.User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel, is_superhero=True)
        bruce = models.User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc, is_superhero=True)
        clark = models.User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc, is_superhero=True)

        # Create activities (with date)
        models.Activity.objects.create(user=tony, type='Run', duration=30, date=date(2023, 1, 1))
        models.Activity.objects.create(user=steve, type='Swim', duration=45, date=date(2023, 1, 2))
        models.Activity.objects.create(user=bruce, type='Cycle', duration=60, date=date(2023, 1, 3))
        models.Activity.objects.create(user=clark, type='Fly', duration=120, date=date(2023, 1, 4))

        # Create workouts
        w1 = models.Workout.objects.create(name='Avenger HIIT', description='High intensity interval training for Avengers')
        w2 = models.Workout.objects.create(name='Justice League Strength', description='Strength training for Justice League')
        w1.suggested_for.add(tony, steve)
        w2.suggested_for.add(bruce, clark)

        # Create leaderboard (for teams)
        models.Leaderboard.objects.create(team=marvel, points=1900)
        models.Leaderboard.objects.create(team=dc, points=2050)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
