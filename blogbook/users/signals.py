from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# post_save is a signal which is sent when a user is registered
# create_profile is a receiver which receives the sender which is the user who is newly registered
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# saves the profile automatically after it is created
@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save() #instance is the user




