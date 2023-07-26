
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet, LivroViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"livros", LivroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
