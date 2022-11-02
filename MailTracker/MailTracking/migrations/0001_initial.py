# Generated by Django 3.1.12 on 2022-10-31 15:58

import MailTracking.models.trackermodel
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageDeatilsModel',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('slug', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.BooleanField(default=False)),
                ('image_name', models.CharField(default='mail_trace.png')),
                ('image_path', models.CharField(default='saticfiles/')),
                ('image_size', models.IntegerField(default=10)),
            ],
            options={
                'db_table': 'db_image_detail',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrackMetricsModel',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('mail_id', models.CharField(blank=True, max_length=255, null=True)),
                ('from_mail_user_token', models.CharField(blank=True, max_length=255, null=True)),
                ('from_mail_address', models.CharField(blank=True, max_length=255, null=True)),
                ('from_host_address', models.CharField(blank=True, max_length=255, null=True)),
                ('from_user_agent', models.CharField(blank=True, max_length=255, null=True)),
                ('to_mail_address', models.CharField(blank=True, max_length=255, null=True)),
                ('to_host_address', models.CharField(blank=True, max_length=255, null=True)),
                ('to_user_agent', models.CharField(blank=True, max_length=255, null=True)),
                ('to_content_length', models.CharField(blank=True, max_length=255, null=True)),
                ('total_mail_opening_count', models.IntegerField(blank=True, null=True)),
                ('mail_event_metrics_stats', djongo.models.fields.EmbeddedField(model_container=MailTracking.models.trackermodel.MailEventMetricsStat)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'db_mail_metrics',
            },
        ),
    ]
