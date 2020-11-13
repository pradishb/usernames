'''Module for models'''
from django.db import models


class Username(models.Model):
    '''Username model'''
    username = models.CharField(max_length=256)

    def __str__(self):
        return self.username
