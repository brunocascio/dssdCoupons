# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Coupon(models.Model):
  used = models.BooleanField()
  discount = models.IntegerField(default=10)

  class Meta:
    db_table = "coupon"

  def __unicode__(self):
    return u"%s" % self.number
