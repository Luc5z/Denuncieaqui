from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('mapa/', views.mapa, name="mapa"),
    path('redirecionamento/', views.redirecionamento, name="redirecionamento"),
    path('duvidas/', views.duvidas, name="duvidas"),
    path("admin/", admin.site.urls),
    path("usuarios/", include('usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
