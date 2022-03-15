from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'." +
    "Up to 15 digits allowed.")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_employee = models.BooleanField(default=False, blank=True)
    company_name = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17,
        blank=True)  # validators should be a list

# from django.db.models.signals import post_save
# from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()