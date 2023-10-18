from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework.routers import DefaultRouter

from livraria.views import AutorViewSet, CategoriaViewSet,DevolucaoViewSet, EmprestimoViewSet, EditoraViewSet, LocalizaçãoViewSet, LivroViewSet
from uploader.router import router as uploader_router
from usuario.router import router as usuario_router

router = DefaultRouter()
router.register(r"autor", AutorViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"devolucoes", DevolucaoViewSet)
router.register(r"emprestimos", EmprestimoViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"localizacao", LocalizaçãoViewSet)
router.register(r"livros", LivroViewSet)



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/usuario", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
     # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/",SpectacularSwaggerView.as_view(url_name="schema"),name="swagger-ui",),
    path("api/redoc/",SpectacularRedocView.as_view(url_name="schema"),name="redoc",),
]


urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)