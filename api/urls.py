from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProveedorViewSet, ProductoViewSet, TransaccionInventarioViewSet

router = DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('proveedores', ProveedorViewSet)
router.register('productos', ProductoViewSet)
router.register('transacciones', TransaccionInventarioViewSet)

urlpatterns = router.urls