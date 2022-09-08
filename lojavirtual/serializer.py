from rest_framework import serializers
from .models import Produto, Categoria


class ProdutoSerializer(serializers.ModelSerializer):
    customField = serializers.CharField(source='category', read_only=True)


    class Meta:
        model = Produto
        fields = ('id','name','description','category','price','customField')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

