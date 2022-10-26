from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class UserModel(AbstractUser):
    GENDER_MALE = 0
    GENDER_MALE = 1
    GENDER_CHOICES = [(GENDER_MALE, _('MALE')), (GENDER_MALE, _('FEMALE'))]
    user_image = models.ImageField(upload_to='users/')
    id_card = models.CharField(max_length=9)
    birth_day = models.DateTimeField()
    phone = models.CharField(max_length=13)
    location_work = models.CharField(max_length=255, null=True, blank=True)
    address_work = models.CharField(max_length=255, null=True, blank=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES)