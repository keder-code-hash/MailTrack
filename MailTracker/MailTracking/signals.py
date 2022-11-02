from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models.trackermodel import TrackMetricsModel
import uuid
from datetime import datetime

@receiver(pre_save,sender=TrackMetricsModel)
def save_mail_track_object(sender,instance,**kwargs):
    # try:
        if 'slug' not in instance.keys():
            # instance.slug=uuid.uuid4.hex
            instance.created_at=datetime.now()
            instance.updated_at=datetime.now()
        else:
            instance.updated_at=datetime.now()

        # if 'mail_event_metrics_stats' in instance.keys():
        #     instance.mail_event_metrics_stats=uuid.uuid4.hex
        #     if 'image1' in instance.mail_event_metrics_stats:
        #         instance.mail_event_metrics_stats["image1"]=uuid.uuid4.hex
        #     if 'image2' in instance.mail_event_metrics_stats:
        #         instance.mail_event_metrics_stats["image2"]=uuid.uuid4.hex
        
        instance.save()

    