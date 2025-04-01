from django.urls import path
from br.views import Estados

urlpatterns = [
    path('estados/',Estados.as_view() ),
   
]
