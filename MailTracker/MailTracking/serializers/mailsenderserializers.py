from ..models.mailsendermodel import MailSenderModel
from rest_framework import serializers

class Mailsenderserializer(serializers.ModelSerializer):
    class Meta:
        model=MailSenderModel
        fields="__all__"
        read_only_field=('_id',)