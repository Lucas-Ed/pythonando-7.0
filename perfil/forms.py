from django import forms
from .models import Conta, Categoria


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContaForm, self).__init__(*args, **kwargs)
        self.fields['apelido'].widget.attrs.update({'class': 'form-control'})
        self.fields['banco'].widget.attrs.update({'class': 'form-control'})
        self.fields['tipo'].widget.attrs.update({'class': 'form-control'})
        self.fields['valor'].widget.attrs.update({'class': 'form-control'})
        self.fields['icone'].widget.attrs.update({'class': 'form-control'})

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'
        exclude = ['valor_planejado']

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].widget.attrs.update({'class': 'form-control'})

