from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Topic(models.Model):
    name = models.CharField(max_length=155)
    created_by = models.ForeignKey(User)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")
        ordering = ("name",)


class Hack(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    deletion_date = models.DateTimeField(null=True)
    last_edit = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    topics = models.ManyToManyField(Topic, null=True)

    class Meta:
        verbose_name = _("Hack")
        verbose_name_plural = _("Hacks")
        ordering = ("-creation_date",)

    def __str__(self):
        return self.title


class Vote(models.Model):
    hack = models.ForeignKey(Hack)
    user = models.ForeignKey(User)
    voted_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.hack.id)+"_"+str(self.user.id)

    class Meta:
        verbose_name = _("Vote")
        verbose_name_plural = _("Votes")
        ordering = ("-voted_datetime",)


class Feedback(models.Model):
    hack = models.ForeignKey(Hack)
    parent = models.ForeignKey("self", null=True)
    user = models.ForeignKey(User)
    description = models.TextField()
    feedback_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.hack.id)+"_"+str(self.user.id)


class HackFallower(models.Model):
    hack = models.ForeignKey(Hack)
    user = models.ForeignKey(User)
    fallow_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.hack.id)+"_"+str(self.user.id)
