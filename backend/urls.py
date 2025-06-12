from django.contrib import admin
from django.urls import path
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Cette ligne gère la racine "/"
     path('courriers/', include('backend.courriers.urls')),
]
