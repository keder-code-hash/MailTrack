from djongo import models

class MailSenderModel(models.Model):
    _id=models.ObjectIdField()
    user_id=models.CharField(max_length=30,blank=True,null=True)
    mail_id=models.CharField(max_length=20,blank=True,null=True)

    to_mail=models.CharField(max_length=100,blank=True,null=True)
    from_mail=models.CharField(max_length=100,blank=True,null=True)
    mail_sent=models.BooleanField(default=True)
    mail_subject=models.TextField()
    mail_body=models.TextField()

    sent_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table="db_mail_sender"