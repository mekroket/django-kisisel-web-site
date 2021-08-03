from django.db import models
from django import forms

class İletisimModelForm(models.Model):
    email = models.EmailField(max_length=170)
    isim_sayisim = models.CharField(max_length=150)
    mesaj = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "iletisim"
        verbose_name = "İletisim"
        verbose_name_plural = "İletişim"
    
    def __str__(self):
        return self.email