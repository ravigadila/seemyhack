from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile


class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True,
                                verbose_name=_('user'), related_name='profile')
    Score = models.IntegerField()
    website = models.URLField()
    description = models.CharField(max_length=1000)
