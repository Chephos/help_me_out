from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Video(models.Model):
    video_file = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.video_file.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.video_file.name = slugify(self.video_file.name)

    # def get_file_by