from django.db import models

# Create your models here.
class Media(models.Model):
    title = models.CharField(max_length=200)
    media = models.FileField(upload_to='ar_media/', null=True, verbose_name="")

class ArObj(models.Model):
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title + ' ' + self.description