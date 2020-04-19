from django.shortcuts import render
from futbol.models import Torneo, Ciudad, Jugador, Estadio, Arbitro, persona_natural, Equipo, Empresa, Jugador_Equipo, Partido, Jugador_Partido, Evento_Gol, Evento_Falta, Otro_Evento 
from futbol.form import FormularioTorneo, FormularioCiudad, FormularioJugador, FormularioEstadio, FormularioArbitro, FormularioPersonaNatural, FormularioEquipo, FormularioEmpresa, FormularioJugadorEquipo, FormularioPartido, FormularioJugadorPartido, FormularioEventoGol, FormularioEventoFalta, FormularioOtroEvento 
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


#Login

class Login (LoginRequiredMixin, generic.TemplateView):
    template_name="login.html"
    login_url = 'futbol:login'



# Inserts


class InsertarTorneo(LoginRequiredMixin, generic.CreateView):
    model = Torneo
    template_name="futbol/InsertarTorneo.html"
    context_object_name="obj"
    form_class=FormularioTorneo
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'

class InsertarCiudad(LoginRequiredMixin, generic.CreateView):
    model = Ciudad
    template_name="futbol/InsertarCiudad.html"
    context_object_name="obj"
    form_class=FormularioCiudad
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'

class InsertarJugador(LoginRequiredMixin, generic.CreateView):
    model = Jugador
    template_name="futbol/InsertarJugador.html"
    context_object_name="obj"
    form_class=FormularioJugador
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'

class InsertarEstadio(LoginRequiredMixin, generic.CreateView):
    model = Estadio
    template_name="futbol/InsertarEstadio.html"
    context_object_name="obj"
    form_class=FormularioEstadio
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'

class InsertarArbitro(LoginRequiredMixin, generic.CreateView):
    model = Arbitro
    template_name="futbol/InsertarArbitro.html"
    context_object_name="obj"
    form_class=FormularioArbitro
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'

class InsertarPersonaNatural(LoginRequiredMixin, generic.CreateView):
    model = persona_natural
    template_name="futbol/InsertarPersonaNatural.html"
    context_object_name="obj"
    form_class=FormularioPersonaNatural
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'

class InsertarEquipo(LoginRequiredMixin, generic.CreateView):
    model = Equipo
    template_name="futbol/InsertarEquipo.html"
    context_object_name="obj"
    form_class=FormularioEquipo
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'

class InsertarEmpresa(LoginRequiredMixin, generic.CreateView):
    model = Empresa
    template_name="futbol/InsertarEmpresa.html"
    context_object_name="obj"
    form_class=FormularioEmpresa
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'

class InsertarJugadorEquipo(LoginRequiredMixin, generic.CreateView):
    model = Jugador_Equipo
    template_name="futbol/InsertarJugadorEquipo.html"
    context_object_name="obj"
    form_class=FormularioJugadorEquipo
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'

class InsertarPartido(LoginRequiredMixin, generic.CreateView):
    model = Partido
    template_name="futbol/InsertarPartido.html"
    context_object_name="obj"
    form_class=FormularioPartido
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'

class InsertarJugadorPartido(LoginRequiredMixin, generic.CreateView):
    model = Jugador_Partido
    template_name="futbol/InsertarJugadorPartido.html"
    context_object_name="obj"
    form_class=FormularioJugadorPartido
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'

class InsertarEventoGol(LoginRequiredMixin, generic.CreateView):
    model = Evento_Gol
    template_name="futbol/InsertarEventoGol.html"
    context_object_name="obj"
    form_class=FormularioEventoGol
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'

class InsertarEventoFalta(LoginRequiredMixin, generic.CreateView):
    model = Evento_Falta
    template_name="futbol/InsertarEventoFalta.html"
    context_object_name="obj"
    form_class=FormularioEventoFalta
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'

class InsertarOtroEvento(LoginRequiredMixin, generic.CreateView):
    model = Otro_Evento
    template_name="futbol/InsertarOtroEvento.html"
    context_object_name="obj"
    form_class=FormularioOtroEvento
    success_url=reverse_lazy("futbol:home")
    login_url = 'futbol:login'


# Consults

class Home(LoginRequiredMixin, generic.ListView):
    model = Partido
    template_name="futbol/Home.html"
    context_object_name="obj"
    login_url = 'futbol:login'