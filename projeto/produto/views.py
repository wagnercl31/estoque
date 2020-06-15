import csv
import io
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from .models import Produto
from .forms import ProdutoForm


def produto_list(request):
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(produto__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context)


class ProdutoList(ListView):
    model = Produto
    template_name = 'produto_list.html'
    paginate_by = 10
    

    def get_queryset(self):
        queryset = super(ProdutoList, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(produto__icontains=search) |
                Q(ncm__icontains=search)
            )
        return queryset


def produto_detail(request, pk):
    template_name = 'produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

def produto_add(request):
    template_name = 'produto_form.html'
    if search:
        objects = objects.filter(produto__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context)


class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


def produto_json(request, pk):
    #Retorna o produto , id e estoque
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})

def save_data(data):
    '''
    Salva os dados no banco.
    '''
    aux = []
    for item in data:
        produto = item.get('produto')
        ncm = str(item.get('ncm'))
        preco = item.get('preco')
        estoque = item.get('estoque')
        estoque_minimo = item.get('estoque_minimo')
        obj = Produto(
            produto=produto,
            ncm=ncm,
            preco=preco,
            estoque=estoque,
            estoque_minimo=estoque_minimo,
        )
        aux.append(obj)
    Produto.objects.bulk_create(aux)


def import_csv(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        #lendo um arquivo InMemoryUploadFile
        file = myfile.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        #gerando uma list comprehesion
        data =[line for line in reader]
        save_data(data)
        return HttpResponseRedirect(reverse('produto:produto_list'))

    template_name = 'produto_import.html'
    return render(request, template_name)