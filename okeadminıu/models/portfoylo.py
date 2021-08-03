from django.db import models

class PortfoyloModel(models.Model):
    ilk_resim = models.ImageField(upload_to = 'portfoylo_resimleri')
    slider_resim1 = models.ImageField(upload_to = 'portfoylo_resimleri')
    slider_resim2 = models.ImageField(upload_to = 'portfoylo_resimleri')
    slider_resim3 = models.ImageField(upload_to = 'portfoylo_resimleri')
    baslik = models.CharField(max_length=400)
    icerik = models.TextField(max_length=400)

    class Meta:
        db_table = "Portfoylo"
        verbose_name = "Portfoylo"
        verbose_name_plural = "Portfoylo"
    
    def __str__(self):
        return self.baslik

