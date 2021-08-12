from django import forms
from django.forms import fields
from okeadminıu.models import İletisimModelForm
from django.core.mail import send_mail

class İletisimForm(forms.ModelForm):
    isim_sayisim = forms.CharField(widget=forms.TextInput(
        attrs={"class":"form-control","placeholder":"İsim Soyisim"}
    ),required=True,max_length=50,label="İsim Soyisim")

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class":"form-control","placeholder":"Email"}
    ),required=True,max_length=50,label="Email")

    mesaj = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control","placeholder":"Mesajınız"}
    ),required=True,max_length=900,label="Mesajınız")


    class Meta:
        model = İletisimModelForm
        fields = ("isim_sayisim","email","mesaj")

    def send_email(self,mesaj):
        send_mail(
            subject='İletişim Formundan Yeni Mesaj Var!',
            message=mesaj,
            from_email=None,
            recipient_list=['info.oguzkaan@gmail.com'],
            fail_silently=False
        )