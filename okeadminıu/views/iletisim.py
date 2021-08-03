from django.shortcuts import render,redirect
from okeadminıu.forms import İletisimForm
from okeadminıu.models import İletisimModelForm
from django.views.generic import FormView


class İletisimFormView(FormView):
    
    template_name = 'pages/iletisim.html'
    form_class = İletisimForm
    success_url = '/email-gonderildi'

    def form_valid(self,form):
        form.save()
        form.send_email(mesaj = form.cleaned_data.get('mesaj'))
        return super().form_valid(form)
