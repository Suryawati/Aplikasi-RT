# Create your models here.
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from wargas.models import Warga

class Letter(models.Model):

    tujuan = models.CharField(max_length=255)
    perihal = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    biodata = models.ForeignKey(Warga, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('surat_pengantar', args=[str(self.id)])


