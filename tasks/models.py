# -*- coding: utf-8 -*-
from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __unicode__(self):
        return self.title
