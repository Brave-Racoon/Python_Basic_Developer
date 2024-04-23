from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class ClientUser(AbstractUser):

    # redefine email field for 'unique' property
    email = models.EmailField('email address', unique=True)
    # add custom field
    aboutfield = models.TextField('about', blank=True)
