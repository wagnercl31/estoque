from django.shortcuts import render
from ..estoque.models import Produto
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    query = Produto.objects.all()
    relatorio = []
    for item in query:
        if (item.estoque - item.estoque_minimo) < 10:
            relatorio.append(item)
    context = {'relatorio':list(map(lambda produto: {
            'produto': produto.produto,
            'estoque': produto.estoque
        }, relatorio))}
    return render(request, 'index.html', context)


