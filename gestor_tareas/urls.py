from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login y logout de Django
    path('accounts/', include('django.contrib.auth.urls')),

    # Aplicación principal
    path('', include('tareas.urls')),
]