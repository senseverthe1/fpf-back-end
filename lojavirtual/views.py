from rest_framework import viewsets
from .models import Produto, Categoria
from .serializer import ProdutoSerializer, CategoriaSerializer
from .filters import ProdutoFilter, CategoriaFilter


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filterset_class = ProdutoFilter

    def get_queryset(self):
        queryset = Produto.objects.all()
        category = self.request.query_params.get('categoria')

        if category:
            queryset = queryset.filter(category=category)
        return queryset


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filterset_class = CategoriaFilter