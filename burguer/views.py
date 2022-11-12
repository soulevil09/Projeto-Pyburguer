from django.shortcuts import render
from .models import Produto


def home(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'burguer/home.html', context)


def produto(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    context = {
        'produto':produto
    }
    return render(request, 'burguer/produto.html', context)
