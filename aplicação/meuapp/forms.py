from django.forms import ModelForm
from meuapp.models import  *
from django import forms


class PintorForm(ModelForm):
    class Meta:
        model = Pintor
        fields = ['nome','nascimento']
        widgets = {
            'nascimento': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            )
        }

class QuadroForm(ModelForm):
    class Meta:
        model = Quadro
        fields = "__all__"
        widgets = {
            'publicacao': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            )
        }

class ComidaForm(ModelForm):
    class Meta:
        model = Comida
        fields = ['nome']


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        widgets = {
            'comida':forms.CheckboxSelectMultiple
        }