from django import forms


class Contato(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome:')
    telefone = forms.CharField(max_length=12, label='Telefone:')
    idade = forms.IntegerField(min_value=18, max_value=120,label='Idade:')
