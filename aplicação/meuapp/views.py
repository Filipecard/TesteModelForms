from django.shortcuts import render,redirect
from meuapp.forms import *

def home(request):
    return render(request,'home.html')

def list_pintores(request):
    pintores = Pintor.objects.all()
    return render(request, "list_pintores.html", {'pintores': pintores})

def list_quadros(request):
    quadros = Quadro.objects.all()
    return render(request, "list_quadros.html", {'quadros': quadros})

def add_pintor(request):
    if request.method == "POST":
        form = PintorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('home')
    else:
        form = PintorForm()
        return render(request, "add.html", {'form': form})

def add_quadro(request):
    if request.method == "POST":
        form = QuadroForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('home')
    else:
        form = QuadroForm()
        return render(request, "add.html", {'form': form})

def list_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, "list_pessoas.html", {'pessoas': pessoas})

def list_comidas(request):
    comidas = Comida.objects.all()
    return render(request, "list_comidas.html", {'comidas': comidas})

def add_pessoa(request):
    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PessoaForm()
        return render(request, "add.html", {'form': form})

def add_comida(request):
    if request.method == "POST":
        form = ComidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ComidaForm()
        return render(request, "add.html", {'form': form})