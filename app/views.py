# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from app.models import Coupon
from app.serializers import CouponSerializer

# Create your views here.

class CouponViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows coupons to be viewed or edited.
  """
  queryset = Coupon.objects.all()
  serializer_class = CouponSerializer