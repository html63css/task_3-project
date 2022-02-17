from django.contrib.auth.models import User, UserManager
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Account(models.Model):
    data = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    status = models.CharField(max_length=20, default='Unblock')

    def set_status(self, x):
        self.status = x
        self.save()

    @receiver(post_save, sender=User)
    def create_user_account(sender, instance, created, **kwargs):
        if created:
            Account.objects.create(data=instance)

    @receiver(post_save, sender=User)
    def save_user_account(sender, instance, **kwargs):
        instance.account.save()
