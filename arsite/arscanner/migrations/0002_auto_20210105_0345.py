# Generated by Django 3.1.2 on 2021-01-04 22:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('arscanner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arobj',
            name='date_event',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='arobj',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='arobj',
            name='url',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='arobj',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='arobj',
            name='media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='arscanner.media'),
        ),
    ]
