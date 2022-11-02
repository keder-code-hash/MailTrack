from djongo import models
from .model import BaseModel

class MailOpeningMetrics(models.Model):
    opened_at=models.DateTimeField(blank=True,null=True)
    opening_user_agent=models.CharField(max_length=255,blank=True,null=True)
    opening_count_order=models.IntegerField()

    class Meta :
        abstract=True

class ImageDeatilsModel(models.Model):
    _id=models.ObjectIdField()
    image_name=models.CharField(max_length=255,default="mail_trace.png")
    image_path=models.CharField(max_length=255,default="saticfiles/")
    image_size=models.IntegerField(default=10)

    class Meta:
        db_table="db_image_detail"
 