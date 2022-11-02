from djongo import models


class BaseModel(models.Model):
    slug=models.CharField(max_length=50,blank=True,null=True)
    status=models.BooleanField(default=False)
    class Meta:
        abstract=True