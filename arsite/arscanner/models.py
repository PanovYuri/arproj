from django.db import models
import uuid

# Create your models here.
class MediaType(models.Model):
    title = models.CharField(max_length=8)

    def __str__(self):
        return self.title

class Media(models.Model):
    title = models.CharField(max_length=200)
    media = models.FileField(upload_to='ar_media/', null=True, verbose_name="")
    media_type = models.ForeignKey(MediaType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class ArObj(models.Model):
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    url   = models.URLField(max_length=100, blank=True)
    date  = models.DateTimeField(auto_now_add=True)
    date_event  = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title + ' ' + self.description
