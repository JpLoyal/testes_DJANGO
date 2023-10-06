from django.shortcuts import render
from django.http import HttpResponseRedirect
from inscricao.forms import Contato

#from inscricao.models import Pessoa


# Create your views here.


def mostra_formulario(request):

    if request.method == 'POST':
        form = Contato(request.POST)

        if form.is_valid():
            #faz algo com os dados

            #Pessoa(form.cleaned_data[''])

            #redireciona para outra página
            return HttpResponseRedirect('.')

        context = {'form': form}
        render(request, 'forms_inscricao.html', context)
    else:
        form = Contato()

    context = {'form': form}
    return render(request, 'forms_inscricao.html', context)