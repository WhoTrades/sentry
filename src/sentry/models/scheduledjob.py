from __future__ import absolute_import, print_function

from django.db import models
from django.utils import timezone
from jsonfield import JSONField

from sentry.db.models import Model, sane_repr


class ScheduledJob(Model):
    name = models.CharField(max_length=128)
    payload = JSONField()
    date_added = models.DateTimeField(default=timezone.now)
    date_scheduled = models.DateTimeField()

    __repr__ = sane_repr('name', 'date_scheduled')
