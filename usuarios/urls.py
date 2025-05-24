from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    # path('inicio/', views.cadastro, name="inicio"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login_view, name="login"),
    path('denuncia/', views.denuncia, name="denuncia"),
    path('historico/', views.historico, name="historico"),
    path('sair/', views.sair, name="sair")
]