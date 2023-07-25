from django.db.models.signals import post_save
from django.contrib.auth.models import User # es el sender, envia la señal
from django.dispatch import receiver #recibe la señal
from .models import Profile


@receiver(post_save, sender = User) #señal y emisor, el receiver es la funcion
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


        
        




