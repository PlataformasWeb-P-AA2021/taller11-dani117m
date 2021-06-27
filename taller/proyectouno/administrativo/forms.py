from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, \
        Departamento

class edificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese direccion por favor'),
            'ciudad': _('Ingrese ciudad por favor'),
            'tipo': _('Ingrese tipo por favor'),
        }

    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())

        if valor[0] == "L":
            raise forms.ValidationError("El nombre no puede contener L")
        return valor

    def clean_direccion(self):
        valor = self.cleaned_data['direccion']
        num_palabras = len(valor.split())

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos apellidos por favor")
        return valor

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        if len(valor) != 10:
            raise forms.ValidationError("Ingrese cédula con 10 dígitos")
        return valor

    def clean_tipo(self):
        valor = self.cleaned_data['tipo']
        if "@" not in valor or "utpl.edu.ec" not in valor:
            raise forms.ValidationError("Ingrese correo válido para la Universidad")
        return valor


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_completo', 'costo', 'num_cuartos', 'edificio']
        labels = {
            'nombre_completo': _('Ingrese nombre por favor'),
            'costo': _('Ingrese costo por favor'),
            'num_cuartos': _('Ingrese num_cuartos por favor'),
            'edificio': _('Ingrese edificio por favor'),
        }


    def clean_nombre_completo(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese su nombre completo")
        return valor

    def clean_costo(self):
        valor = self.cleaned_data['costo']

        if valor > 100000:
            raise forms.ValidationError("Costo fuera de margenes")
        return valor

    def clean_num_cuartos(self):
        valor = self.cleaned_data['num_cuartos']

        if valor == 0 or valor > 7:
            raise forms.ValidationError("El numero de habitaciones es invalido")
        return valor






class NumeroDepartamentoForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(NumeroDepartamentoForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['nombre_completo', 'costo', 'num_cuartos', 'edificio']

    def clean_nombre_completo(self):
        nombre = self.cleaned_data['nombre_propietario']
        num_palabras = len(nombre.split())
        if num_palabras < 3:
            raise forms.ValidationError("Ingrese su nombre completo")
        return nombre

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if valor > 1000000:
            raise forms.ValidationError("Costo fuera de margenes")
        return valor	


    def clean_num_cuartos(self):
        num = self.cleaned_data['numero_cuartos']
        if num== 0 or num > 7:
            raise forms.ValidationError("El numero de habitaciones es invalido")
        return num

##
##- Usar formularios creados desde el archivo forms.py
## 	- Agregar validaciones: 
## 		- Costo de un departamento no puede ser mayor a $100 mil.
## 		- Número de cuartos no puede ser 0, ni mayor a 7
## 		- El nombre de la ciudad no puede iniciar con la letra mayúscula **L**
## 		- El nombre completo de un propietario **no** debe tener menos de 3 palabras.