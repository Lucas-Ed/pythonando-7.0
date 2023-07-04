from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import settings
from .views import HomePerfilView, GerenciarView, CadatrarBancoView, CadastrarCategoriaView, DeletarBancoView, \
    AtualizarCategoriaView, atualizarCategoria

urlpatterns = [

    path('home/', HomePerfilView.as_view(), name='home'),
    path('gerenciar/', GerenciarView.as_view(), name='gerenciar'),
    path('cadastrar/banco/', CadatrarBancoView.as_view(), name='cadastrar_banco'),
    path('excluir/banco/<int:pk>/', DeletarBancoView.as_view(), name='excluir_banco'),

    path('cadastrar/categoria', CadastrarCategoriaView.as_view(), name='cadastrar_categoria'),
    path('atualizar/categoria/<int:pk>/', atualizarCategoria, name='atualizar_categoria'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)