from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from base.formularios_django.forms import ClienteForm
from base.formularios_django.models import Cliente


def form_modelform(request):
    if request.method == 'GET':
        form = ClienteForm()
        context = {
            'form': form
        }
        return render(request, "formularios_django/formulario_modelform.html", context=context)
    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClienteForm()

        context = {
            'form': form
        }
        return render(request, "formularios_django/formulario_modelform.html", context=context)


def sucesso(request):
    return render(request, "formularios_django/sucesso.html")


def listar_usuarios(request):
    data_list = Cliente.objects.all().order_by('nome')
    context = {
        'data_list': data_list
    }
    return render(request, "formularios_django/listar_usuarios.html", context=context)
