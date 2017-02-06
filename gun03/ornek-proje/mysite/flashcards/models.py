from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    correct = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s: %s" % (self.id, self.question)
