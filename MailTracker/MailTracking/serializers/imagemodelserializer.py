from rest_framework import serializers
from .serializer import BaseModelSerializer
from ..models.imagemodel import ImageDeatilsModel


class MailOpeningMetricsSerializer(serializers.Serializer):
    opened_at=serializers.DateTimeField()
    opening_user_agent=serializers.CharField(allow_blank=True,allow_null=True)
    opening_count_order=serializers.IntegerField()


class ImageDeatilsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=ImageDeatilsModel
        fields="__all__"
        read_only_fields = ('_id',)