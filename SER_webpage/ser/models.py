from django.db import models

# Create your models here.
from django.db import models

class apa(models.Model):
    apfile = models.FileField( upload_to='ser/static/ser/audio_files')
    

