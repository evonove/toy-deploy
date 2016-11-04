from django.db import models


class Event(models.Model):
    """
    Model to represent an event
    """
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return '%s: %s' % (self.name, self.description)
