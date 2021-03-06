from app.models import Coupon
from rest_framework import serializers


class CouponSerializer(serializers.ModelSerializer):
  class Meta:
    model = Coupon
    fields = ('id', 'used', 'discount')