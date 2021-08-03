from django.urls import path


from okeadminıu.views import DetaySayfası
from okeadminıu.models import PortfoyloModel
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
    path("detay-sayfasi/<int:id>",DetaySayfası,name="detay-sayfasi"),
] 