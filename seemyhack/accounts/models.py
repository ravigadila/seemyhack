from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    description = models.CharField(max_length=1000)
    website = models.URLField()

    def __str__(self):
        return self.email


class UserExtra(models.Model):
    email_confirmed = models.BooleanField(default=False)
    activation_key = models.CharField(_('activation key'), max_length=40, blank=True)
    user = models.OneToOneField(User, verbose_name=_('user'), related_name='userextra')

    def __str__(self):
        return self.user.email
