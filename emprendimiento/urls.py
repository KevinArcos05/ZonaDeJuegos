from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
