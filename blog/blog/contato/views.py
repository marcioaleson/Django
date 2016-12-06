from django.shortcuts import render

from .forms import ContatoForm

# Create your views here.

def contato(request):
    form = ContatoForm()
    return render(request, 'contato/contato.html', {'form': form})
