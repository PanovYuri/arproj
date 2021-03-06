# Generated by Django 3.1.2 on 2020-10-20 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('media', models.FileField(null=True, upload_to='ar_media/', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='ArObj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('media', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='arscanner.media')),
            ],
        ),
    ]
