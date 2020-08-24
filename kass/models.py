from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Kas(models.Model):
    title_kas = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    foto_kas = models.ImageField(upload_to='foto_kas/', blank=True)

    def __str__(self):
        return self.title_kas

    def get_absolute_url(self):
        return reverse('kas', args=[str(self.id)])

    # def get_absolute_url(self):
    #     return reverse('article_detail', kwargs={'pk': str(self.pk)})
