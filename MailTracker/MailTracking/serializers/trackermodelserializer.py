from rest_framework import serializers
from .imagemodelserializer import MailOpeningMetricsSerializer
from .serializer import BaseModelSerializer
from ..models.trackermodel import TrackMetricsModel


class MailEventMetricsSerializer(serializers.Serializer):
    mail_status=serializers.CharField(allow_blank=True,allow_null=True)
    mail_opened_history=MailOpeningMetricsSerializer(required=False)
    image_slug=serializers.CharField(allow_blank=True,allow_null=True)

class MailEventMetricsStatSerializer(serializers.Serializer):
    image1=MailEventMetricsSerializer(required=False)
    image2=MailEventMetricsSerializer(required=False) 

class TrackMetricsModelSerializer(serializers.ModelSerializer):
    """
        mail_event_metrics : it should be created seperately for each and every image related to a specfic mail.
    """
    mail_event_metrics_stats=MailEventMetricsStatSerializer(required=False) 

    class Meta:
        model=TrackMetricsModel
        fields = "__all__"
        read_only_fields = ('_id',)


# {
#   "slug": "string",
#   "status": false,
#   "mail_event_metrics": [
#     {
#       "slug": "12we3212wdrfer",
#       "status": false,
#       "mail_status": "open",
#       "mail_opened_history": {
#         "slug": "12we3212wdrfe12",
#         "status": false,
#         "opened_at": "2022-10-27T14:02:59.826Z",
#         "opening_user_agent": "mobile",
#         "opening_count_order": 0
#       },
#       "image_slug": "6289802772werdf"
#     }
#   ],
#   "mail_id": "kedernath.mallick.tint022@gmail.com",
#   "from_mail_user_token": "62erd42sd34fr55",
#   "from_mail_address": "kedernath.mallick.tint022@gmail.com",
#   "from_host_address": "mail.google.com",
#   "from_user_agent": "laptop",
#   "to_mail_address": "kedernath.tint022@gmail.com",
#   "to_host_address": "127.0.0.1",
#   "to_user_agent": "laptop",
#   "to_content_length": 12,
#   "total_mail_opening_count": 1,
#   "created_at": "2022-10-27T14:02:59.826Z",
#   "updated_at": "2022-10-27T14:02:59.826Z"
# }