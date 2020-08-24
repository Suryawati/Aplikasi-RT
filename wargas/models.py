from django.conf import settings
from django.db import models
from django.urls import reverse


class Warga(models.Model):
    nama = models.CharField(max_length=30)
    tempatlahir = models.CharField(max_length=30)
    tgllahir = models.DateField()
    noktp = models.CharField(max_length=30)
    nokk = models.CharField(max_length=30)
    ktp = models.ImageField(upload_to='ktp/', blank=True)
    STATUS_TINGGAL = (
        ('TE', 'TETAP'),
        ('KO', 'KONTRAK'),
        ('KS', 'KOS'),
        ('PE', 'PEMILIK RUMAH non WARGA')
    )
    statustinggal = models.CharField(max_length=30, choices=STATUS_TINGGAL)

    NORUMAH = (
        ('1', 'NO 1'),
        ('2', 'NO 2'),
        ('3', 'NO 3'),
        ('23', 'NO 23')
    )
    no_rumah = models.CharField(max_length=5, choices=NORUMAH)

    def __str__(self):
        return self.nama

    #def get_absolute_url(self):
    #    return reverse('article_detail', args=[str(self.id)])

    def get_absolute_url(self):
        return reverse('warga_detail', kwargs={'pk': str(self.pk)})



# Create your models here.
