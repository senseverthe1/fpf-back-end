from django.contrib import admin
from django.urls import path, include
from lojavirtual.views import ProdutoViewSet, CategoriaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'produto',ProdutoViewSet, basename='Produto')
router.register(r'categoria',CategoriaViewSet, basename='Categoria')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
