"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from okeadminıu.views import Anasayfa
from okeadminıu.views import DetaySayfası
from okeadminıu.models import PortfoyloModel
from django.views.generic import TemplateView,RedirectView # değişiklik olmayan kısımlarda kullanılır hakkımda gibi 
from okeadminıu.forms import İletisimForm
from okeadminıu.views import İletisimFormView
#templateview içi boş olan sayfalar için
#redirectview yönlendirme


urlpatterns = [
    path('oke-admin-server/', admin.site.urls),
    path("",Anasayfa,name="anasayfa"),
    path("projeler/",include("okeadminıu.urls")),
    
    path('iletisim', İletisimFormView.as_view(), name='iletisim'),

    path('email-gonderildi', TemplateView.as_view(
        template_name = 'pages/email-gonderildi.html'
    ), name='email-gonderildi'),

    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_title = "O.Kaan Ekin Admin Panel"
admin.site.site_header = "O.Kaan Ekin Admin Panel"
admin.site.index_title = "Hoşgeldiniz Oğuz Kaan Ekin"
