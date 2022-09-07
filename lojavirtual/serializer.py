from rest_framework import serializers
from .models import Produto, Categoria


class ProdutoSerializer(serializers.ModelSerializer):
    # categoria = serializers.CharField(read_only=True)
    # CategoriaSerializer
    # def to_representation(self, instance):
    #     self.fields['categoria'] = CategoriaSerializer(read_only=True)
    #     return super(ProdutoSerializer, self).to_representation(instance)
    customField = serializers.CharField(source='category', read_only=True)


    class Meta:
        model = Produto
        fields = ('id','name','description','category','price','customField')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

