from django.core.management.base import BaseCommand
from Usersmodels import User, Profile

class Command(BaseCommand):
    help = 'Seed data for User and Profile models'

    def handle(self, *args, **kwargs):
        # Create a superuser
        User.objects.create_superuser(
            email='admin@example.com',
            password='adminpassword',
            name='Admin User'
        )
        self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))

        # Create some sample users
        User.objects.create_user(
            email='staff@example.com',
            password='staffpassword',
            user_type='staff',
            name='Staff User'
        )
        User.objects.create_user(
            email='customer@example.com',
            password='customerpassword',
            user_type='customer',
            name='Customer User'
        )
        self.stdout.write(self.style.SUCCESS('Sample users created successfully.'))

        # Create profiles for the sample users
        for user in User.objects.all():
            Profile.objects.create(user=user, name=user.name)
        self.stdout.write(self.style.SUCCESS('Profiles created successfully.'))
