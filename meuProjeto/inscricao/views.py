from django.shortcuts import render
from django.http import HttpResponseRedirect
from inscricao.forms import Contato

from inscricao.models import Pessoa


# Create your views here.


def mostra_formulario(request):

    if request.method == 'POST':
        form = Contato(request.POST)

        if form.is_valid():

            #faz algo com os dados
            PessoaAtual = Pessoa.objects.create(**form.cleaned_data)

            #redireciona para outra página
            return HttpResponseRedirect(f'/inscricao/{PessoaAtual.pk}')

        context = {'form': form}
        render(request, 'forms_inscricao.html', context)
    else:
        form = Contato()

    context = {'form': form}
    return render(request, 'forms_inscricao.html', context)


def mostraDadosDaPessoa(request, pk):
    PessoaAtual = Pessoa.objects.get(pk=pk)
    return render(request, 'inscricaoConfirmada.html', {'PessoaAtual': PessoaAtual})