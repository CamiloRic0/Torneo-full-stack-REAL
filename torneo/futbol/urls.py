from django.contrib import admin
from django.urls import include, path
from futbol.views import InsertarTorneo, InsertarCiudad, InsertarJugador, InsertarEstadio, InsertarArbitro, InsertarPersonaNatural, InsertarEquipo, InsertarEmpresa, InsertarJugadorEquipo, InsertarPartido, InsertarJugadorPartido, InsertarEventoGol, InsertarEventoFalta, InsertarOtroEvento, Home, RolArbitro
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='login.html'),name='logout'),
    path('RolArbitro', RolArbitro.as_view(), name="RolArbitro"),
    path('InsertarTorneo', InsertarTorneo.as_view(), name="InsertarTorneo"),
    path('InsertarCiudad', InsertarCiudad.as_view(), name="InsertarCiudad"),
    path('InsertarJugador', InsertarJugador.as_view(), name="InsertarJugador"),
    path('InsertarEstadio', InsertarEstadio.as_view(), name="InsertarEstadio"),
    path('InsertarArbitro', InsertarArbitro.as_view(), name="InsertarArbitro"),
    path('InsertarPersonaNatural', InsertarPersonaNatural.as_view(), name="InsertarPersonaNatural"),
    path('InsertarEquipo', InsertarEquipo.as_view(), name="InsertarEquipo"),
    path('InsertarEmpresa', InsertarEmpresa.as_view(), name="InsertarEmpresa"),
    path('InsertarJugadorEquipo', InsertarJugadorEquipo.as_view(), name="InsertarJugadorEquipo"),
    path('InsertarPartido', InsertarPartido.as_view(), name="InsertarPartido"),
    path('InsertarJugadorPartido', InsertarJugadorPartido.as_view(), name="InsertarJugadorPartido"),
    path('InsertarEventoGol', InsertarEventoGol.as_view(), name="InsertarEventoGol"),
    path('InsertarEventoFalta', InsertarEventoFalta.as_view(), name="InsertarEventoFalta"),
    path('InsertarOtroEvento', InsertarOtroEvento.as_view(), name="InsertarOtroEvento"),
 
]
