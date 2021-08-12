from django.db import models

class PortfoyloModel(models.Model):
    ilk_resim = models.ImageField(upload_to = 'portfoylo_resimleri')
    slider_resim1 = models.ImageField(upload_to = 'portfoylo_resimleri')
    slider_resim2 = models.ImageField(upload_to = 'portfoylo_resimleri')
    slider_resim3 = models.ImageField(upload_to = 'portfoylo_resimleri')
    baslik = models.CharField(max_length=400)
    icerik = models.TextField(max_length=400)

    kategori = models.CharField(max_length=50)
    tarih = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=50)

    class Meta:
        db_table = "Portfoylo"
        verbose_name = "Portfoylo"
        verbose_name_plural = "Portfoylo"
    
    def __str__(self):
        return self.baslik