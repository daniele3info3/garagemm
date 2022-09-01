from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, CorViewSet, MarcaViewSet, ModeloViewSet

router = DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('cor', CorViewSet)
router.register('marca', MarcaViewSet)
router.register('modelo', ModeloViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]