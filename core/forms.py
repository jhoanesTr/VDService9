from django.forms import *
from .models import ContactoModel

class ContactoForm(ModelForm):
    class Meta:
        model = ContactoModel
        fields = '__all__'
        widgets = {
            'Nombre' : TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un nombre para dirigirnos a usted',
                    'autofocus': True
                }
            ),
            'Email': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'example@gmail.com'
                }
            ),
            'Telefono': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '630000000'
                }
            ),
            'Motivo': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'CP': Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': '36000'
                }
            ),
            'Disponibilidad': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'De: 00:00 a 00:00'
                }
            ),
            'Comentario': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Describa la situacion (si es necesario)',
                    'rows': 3

                }
            )
        }
