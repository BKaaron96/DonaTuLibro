import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
### Selects que contienen los tipos de usuario y los colegios disponibles
tusuario=(("Alumno","Alumno"),("Donante","Donante"),("Director","Director"))
colegios=(("Villa el salvador","Villa el salvador"),("Villa Maria del Triunfo","Villa Maria del Triunfo"),("San Juan de Lurigancho","San Juan de Lurigancho"))
class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=20)
    contraseña = forms.CharField(max_length=20,widget = forms.PasswordInput() )

class RegistrationForm(forms.Form):
    # PARA VALIDAR QUE EL # DE TELEFONO TENGA UN FORMATO ESPECIFICO Y UN # MAX DE DIGITOS
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Num de telefono debe estar en el siguiente formato: '+999999999'. Hasta 15 dígitos")

    ### CAMPOS DE CADA FORM DEL REGISTRO(SON 8 CAMPOS NORMALES Y 2 QUE CONTIENEN SELECTS)

    nombre = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)),label=_("Nombre"))
    apellido = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)),label=_("Apellido"))
    telefono = forms.CharField(validators=[phone_regex]) # validators deben ser una lista
    dni=forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_lenghth=9)),label=_("DNI"))
    correo = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Correo"))
    usuario = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=20)), label=_("Usuario"), error_messages={ 'invalid': _("Usuario solo puede tener letras y números") })
    contra1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=20, render_value=False)), label=_("Contraseña"))
    contra2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=20, render_value=False)), label=_("Contraseña(Ingrese nuevamente)"))
    tipodeusuario = forms.ChoiceField(widget=forms.Select,choices=tusuario)
    colegio = forms.ChoiceField(widget=forms.Select,choices=colegios)


    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['usuario'])
        except User.DoesNotExist:
            return self.cleaned_data['usuario']
        raise forms.ValidationError(_("Usuario ya existe"))

    def clean(self):
        if 'contra1' in self.cleaned_data and 'contra2' in self.cleaned_data:
            if self.cleaned_data['contra1'] != self.cleaned_data['contra2']:
                raise forms.ValidationError(_("Las contraseñas no son iguales"))
        return self.cleaned_data
