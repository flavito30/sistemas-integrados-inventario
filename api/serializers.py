from rest_framework import serializers
from .models import Categoria, Proveedor, Producto, TransaccionInventario

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class TransaccionInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionInventario
        fields = '__all__'