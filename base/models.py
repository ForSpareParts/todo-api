from django.conf import settings
from django.db import models


# the User model is built into Django's 'auth' package


class ToDo(models.Model):
    '''Represents a single "to do" item, associated with a user.'''

    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    completed_on = models.DateTimeField(auto_now=False, blank=True, null=True)
