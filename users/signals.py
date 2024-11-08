from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# create a user profile when a user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # if user is created
    if created:
        # create a instance of profile for the user
        Profile.objects.create(user=instance)
        
        
# also save the profile when the user is created
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # save the profile of the user
    instance.profile.save()