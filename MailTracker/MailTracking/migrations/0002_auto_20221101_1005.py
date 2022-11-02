# Generated by Django 3.1.12 on 2022-11-01 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MailTracking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagedeatilsmodel',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='imagedeatilsmodel',
            name='status',
        ),
        migrations.AlterField(
            model_name='imagedeatilsmodel',
            name='image_name',
            field=models.CharField(default='mail_trace.png', max_length=255),
        ),
        migrations.AlterField(
            model_name='imagedeatilsmodel',
            name='image_path',
            field=models.CharField(default='saticfiles/', max_length=255),
        ),
    ]