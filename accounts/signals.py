from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from accounts.models import User, UserProfile


# Post-save Signal for creating user profile
@receiver(post_save, sender=User)
def post_save_create_user_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create user profile if does not exist
            UserProfile.objects.create(user=instance)


@receiver(pre_save, sender=User)
# Pre-save Signal for updating user profil
def pre_save_create_user_profile_receiver(sender, instance, **kwargs):
    pass
