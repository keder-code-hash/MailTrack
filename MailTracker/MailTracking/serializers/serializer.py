from rest_framework import serializers

class BaseModelSerializer(serializers.Serializer):
    slug=serializers.CharField(allow_blank=True,allow_null=True)
    status=serializers.BooleanField(default=False)