# Generated by Django 3.1.12 on 2022-11-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MailTracking', '0003_mailsendermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailsendermodel',
            name='mail_subject',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]
