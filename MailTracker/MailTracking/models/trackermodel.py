from pyexpat import model
from djongo import models
from .imagemodel import MailOpeningMetrics
from .model import BaseModel

MAIL_STATUS_CHOICE =(
    ("do", "didnt_open"),
    ("obi", "open_bn_interact"),
    ("op", "open_interaction"),
    ("s", "subscribe") 
)

class Track(models.Model):
    count=models.IntegerField()
    
 
class MailEventMetrics(models.Model):
    mail_status=models.CharField(max_length=3,choices=MAIL_STATUS_CHOICE)
    image_slug=models.CharField(max_length=30,blank=True,null=True)
    mail_opened_history=models.EmbeddedField(model_container=MailOpeningMetrics)

    class Meta:
        abstract=True

class MailEventMetricsStat(models.Model):
    image1=models.EmbeddedField(model_container=MailEventMetrics)
    image2=models.EmbeddedField(model_container=MailEventMetrics)
    
    class Meta:
        abstract=True

class TrackMetricsModel(models.Model):
    """ 
        mail_id:auto generated from frontend
    """    
    _id=models.ObjectIdField()

    mail_id=models.CharField(max_length=255,blank=True,null=True)
    from_mail_user_token=models.CharField(max_length=255,blank=True,null=True)

    from_mail_address=models.CharField(max_length=255,blank=True,null=True)
    from_host_address=models.CharField(max_length=255,blank=True,null=True)
    from_user_agent=models.CharField(max_length=255,blank=True,null=True)

    to_mail_address=models.CharField(max_length=255,blank=True,null=True)
    to_host_address=models.CharField(max_length=255,blank=True,null=True)
    to_user_agent=models.CharField(max_length=255,blank=True,null=True)
    to_content_length=models.CharField(max_length=255,blank=True,null=True)

    total_mail_opening_count=models.IntegerField(blank=True,null=True)
    '''
        auto updation of status should be supported.
    '''
    """
        mail_event_metrics : it should be created seperately for each and every image
                                related to a specfic mail.
    """
    mail_event_metrics_stats=models.EmbeddedField(model_container=MailEventMetricsStat)

    created_at=models.DateTimeField(blank=True,null=True)
    updated_at=models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table="db_mail_metrics"