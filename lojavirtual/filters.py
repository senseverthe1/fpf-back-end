from django_filters import rest_framework as filters
from .models import Produto


class ProdutoFilter(filters.FilterSet):
    nome = filters.CharFilter(field_name='nome', lookup_expr='icontains')
    # categoria = filters.CharFilter(field_name='categoria__categoria', lookup_expr='icontains')

    class Meta:
        model: Produto
        fields: ('nome')
        # fields: ('title','categoria__categoria')


class CategoriaFilter(filters.FilterSet):
    categoria_name = filters.CharFilter(field_name='categoria_name', lookup_expr='icontains')

    class Meta:
        model: Produto
        fields: ('categoria_name')