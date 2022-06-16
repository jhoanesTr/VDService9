from django.urls import path
from .views import HomeView, PresupuestoView, ContactoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('presupuesto', PresupuestoView.as_view(), name='presupuesto'),
    path('contacto', ContactoView.as_view(), name='contacto'),
]