from django.urls import path
from br.views import CreateEstados, GetEstadosSlug,GetEstados

urlpatterns = [
    path('estados/',GetEstados.as_view() ),
    path('estado/search',GetEstadosSlug.as_view() ),
    path('estado/criar', CreateEstados.as_view())
    
   
]
