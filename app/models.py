# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Coupon(models.Model):
  number = models.IntegerField()
  used = models.BooleanField()

  class Meta:
    db_table = "coupon"

  def __unicode__(self):
    return u"%s" % self.number
