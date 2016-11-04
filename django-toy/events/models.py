from django.db import models


class Event(models.Model):
    """
    Model to represent an event
    """
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return '%s: %s' % (self.name, self.description)
