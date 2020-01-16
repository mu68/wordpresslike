from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField('Titre',max_length=200)
    texte = models.TextField('texte')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Created_date = models.DateTimeField('date de publication',default=timezone.now)
    published_date=models.DateTimeField('Date de publication',blank=True, null=True)
    upload = models.ImageField('image', null=True, upload_to="galerie")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

