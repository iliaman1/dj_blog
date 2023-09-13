from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def createProfile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, username=instance.username)


@receiver(post_save, sender=Profile)
def updateUser(instance, created, **kwargs):
    profile = instance
    user = profile.user

    if not created:
        user.first_name = profile.full_name
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)
def deleteUser(instance, **kwargs):
    instance.user.delete()
