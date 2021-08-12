from django.contrib import admin

from okeadminıu.models import İletisimModelForm,PortfoyloModel

@admin.register(PortfoyloModel)
class PortfoyloAdmin(admin.ModelAdmin):
    list_display = (
        "ilk_resim","slider_resim1","slider_resim2","slider_resim3","baslik","icerik","kategori","tarih","url"
    )
    search_fields = ("baslik","icerik")

@admin.register(İletisimModelForm)
class İletisimAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)