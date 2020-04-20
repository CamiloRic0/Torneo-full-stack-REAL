from django import forms
from futbol.models import RolArbitro, Pais, Torneo, Ciudad, Jugador, Estadio, Arbitro, persona_natural, Equipo, Empresa, Jugador_Equipo, Partido, Jugador_Partido, Evento_Gol, Evento_Falta, Otro_Evento 






class FormularioRolArbitro(forms.ModelForm):
    class Meta:
        model = RolArbitro
        fields = ['nombre']
        labels = {'nombre':'Nombre'}
        widget = {'nombre':forms.TextInput()}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })

class FKPais(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombre)

class FormularioTorneo(forms.ModelForm):
    pais = FKPais(queryset=Pais.objects.order_by('id'))
    class Meta:
        model = Torneo
        fields = ['nombre', 'pais']
        labels = {'nombre':'Nombre'}
        widget = {'nombre':forms.TextInput()}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
            self.fields['pais'].label = 'Pais'

class FormularioCiudad(forms.ModelForm):
    pais = FKPais(queryset=Pais.objects.order_by('id'))
    class Meta:
        model = Ciudad
        fields = ['nombre', 'poblacion', 'pais']
        labels = {'nombre':'Nombre', 'poblacion':'Número de la poblacion'}
        widget = {'nombre':forms.TextInput(), 'poblacion':forms.NumberInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
            self.fields['pais'].label = 'Pais'

class FormularioJugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['codigo','nombre', 'edad']
        labels = {'codigo':'Codigo' ,'nombre':'Nombre', 'edad':'Edad'}
        widget = {'codigo':forms.NumberInput(), 'nombre':forms.TextInput(), 'edad':forms.NumberInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })

class FKCiudad(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombre)

class FormularioEstadio(forms.ModelForm):
    ciudad = FKCiudad(queryset=Ciudad.objects.order_by('codigo'))
    class Meta:
        model = Estadio
        fields = ['codigo', 'nombre', 'ciudad', 'anno_construccion', 'capacidad']
        labels = {'codigo':'Codigo', 'nombre':'Nombre', 'anno_construccion':'Año de construcción', 'capacidad':'Capacidad'}
        widget = {'codigo':forms.NumberInput(), 'nombre':forms.TextInput(), 'anno_construccion':forms.NumberInput(), 'capacidad':forms.NumberInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
            self.fields['ciudad'].label = 'Ciudad'

class FKArbitro(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombre)

class FKRolArbitro(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombre)

class FormularioArbitro(forms.ModelForm):
    tutor_de_arbitro = FKArbitro(queryset=Arbitro.objects.order_by('carne'))
    rol = FKRolArbitro(queryset=RolArbitro.objects.order_by('id'))
    class Meta:
        model = Arbitro
        fields = ['carne', 'nombre', 'tutor_de_arbitro', 'rol']
        labels = {'carne':'Carne', 'nombre':'Nombre completo del arbitro'}
        widget = {'carne':forms.NumberInput(),'nombre':forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
            self.fields['tutor_de_arbitro'].label = 'Nombre del tutor del arbitro'
            self.fields['rol'].label = 'Rol'

class FormularioPersonaNatural(forms.ModelForm):
    class Meta:
        model = persona_natural
        fields = ['cedula', 'nombre', 'telefono']
        labels = {'cedula':'Cedula', 'nombre':'Nombre', 'telefono':'Telefono'}
        widget = {'cedula':forms.NumberInput(),'nombre':forms.TextInput(), 'telefono':forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })

class FKEquipo(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombre)

class FKPersonaNatural(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombre)

class FormularioEquipo(forms.ModelForm):
    ciudad = FKCiudad(queryset=Ciudad.objects.order_by('codigo'))
    patrocinador_equipo = FKEquipo(queryset=Equipo.objects.order_by('codigo'))
    patrocinador_persona_natural = FKPersonaNatural(queryset=persona_natural.objects.order_by('cedula'))
    class Meta:
        model = Equipo
        fields = ['codigo', 'ciudad', 'nombre', 'anno_creacion', 'patrocinador_equipo', 'patrocinador_persona_natural']
        labels = {'codigo':'Codigo', 'nombre':'Nombre', 'anno_creacion':'Año de creación'}
        widget = {'codigo':forms.NumberInput(),'nombre':forms.TextInput(), 'anno_creacion':forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
            self.fields['ciudad'].label = 'Ciudad'
            self.fields['patrocinador_equipo'].label = 'Equipo patrocinador'
            self.fields['patrocinador_persona_natural'].label = 'Persona natural patrocinadora'

class FormularioEmpresa(forms.ModelForm):
    ciudad_sede_principal = FKCiudad(queryset=Ciudad.objects.order_by('codigo'))
    equipo_patrocinado = FKEquipo(queryset=Equipo.objects.order_by('codigo'))
    class Meta:
        model = Empresa
        fields = ['codigo', 'nombre', 'representante_legal', 'email', 'ciudad_sede_principal', 'equipo_patrocinado']
        labels = {'codigo':'Codigo', 'nombre':'Nombre', 'representante_legal':'Representante legal', 'email':'Email'}
        widget = {'codigo':forms.NumberInput(),'nombre':forms.TextInput(), 'representante_legal':forms.TextInput(), 'email':forms.EmailInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
            self.fields['ciudad_sede_principal'].label = 'Ciudad sede principal'
            self.fields['equipo_patrocinado'].label = 'Equipo que patrocina'

class FKJugador(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombre)

class FormularioJugadorEquipo(forms.ModelForm):
    equipo_actual = FKEquipo(queryset=Equipo.objects.order_by('codigo'))
    equipo_anterior = FKEquipo(queryset=Equipo.objects.order_by('codigo'))
    jugador = FKJugador(queryset=Jugador.objects.order_by('codigo'))
    class Meta:
        model = Jugador_Equipo
        fields = ['jugador', 'equipo_actual', 'fecha_inicial', 'fecha_final', 'equipo_anterior']
        labels = {'fecha_inicial':'Fecha inicio equipo', 'fecha_final':'Fecha finalizo equipo'}
        widget = {'fecha_inicial':forms.DateInput(), 'fecha_final':forms.DateInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
            self.fields['equipo_actual'].label = 'Equipo actual'
            self.fields['jugador'].label = 'Jugador'
            self.fields['equipo_anterior'].label = 'Equipo anterior'

class FKEstadio(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombre)

class FKTorneo(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.nombre)

class FormularioPartido(forms.ModelForm):
    arbitro = FKArbitro(queryset=Arbitro.objects.order_by('carne'))
    estadio = FKEstadio(queryset=Estadio.objects.order_by('codigo'))
    equipo_local = FKEquipo(queryset=Equipo.objects.order_by('codigo'))
    equipo_visitante = FKEquipo(queryset=Equipo.objects.order_by('codigo'))
    ganador = FKEquipo(queryset=Equipo.objects.order_by('codigo'))
    nombre_torneo = FKTorneo(queryset=Torneo.objects.order_by('id'))
    class Meta:
        model = Partido
        fields = ['arbitro', 'estadio', 'equipo_local', 'equipo_visitante', 'fecha', 'hora', 'marcador', 'ganador', 'empate', 'nombre_torneo']
        labels = {'fecha':'Fecha partido', 'hora':'Hora partido', 'marcador':'Marcador final', 'empate':'Marcador empatado'}
        widget = {'fecha':forms.DateInput(), 'hora':forms.TimeInput(), 'marcador':forms.TextInput(), 'empate':forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
            self.fields['arbitro'].label = 'Arbitro'
            self.fields['estadio'].label = 'Estadio'
            self.fields['equipo_local'].label = 'Equipo local'
            self.fields['equipo_visitante'].label = 'Equipo visitante'
            self.fields['ganador'].label = 'Ganador'
            self.fields['nombre_torneo'].label = 'Torneo'

class FKPartido(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{} {} {}".format(obj.fecha, obj.equipo_local, obj.equipo_visitante)

class FormularioJugadorPartido(forms.ModelForm):
    partido = FKPartido(queryset=Partido.objects.order_by('fecha'))
    jugador = FKJugador(queryset=Jugador.objects.order_by('codigo'))
    class Meta:
        model = Jugador_Partido
        fields = ['partido', 'jugador', 'min_ingreso', 'min_salida']
        labels = {'min_ingreso':'Minuto de ingreso', 'min_salida':'Minuto de salida'}
        widget = {'min_ingreso':forms.TextInput(), 'min_salida':forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
            self.fields['partido'].label = 'Partido'
            self.fields['jugador'].label = 'Jugador'

class FKJugadorPartido(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.jugador)

class FormularioEventoGol(forms.ModelForm):
    partido = FKPartido(queryset=Partido.objects.order_by('fecha'))
    Jugador_partido = FKJugadorPartido(queryset=Jugador_Partido.objects.order_by('jugador'))
    class Meta:
        model = Evento_Gol
        fields = ['partido', 'minu', 'seg', 'Jugador_partido']
        labels = {'minu':'Minuto del gol', 'seg':'Segundo del gol'}
        widget = {'minu':forms.NumberInput(), 'seg':forms.NumberInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
            self.fields['partido'].label = 'Partido'
            self.fields['Jugador_partido'].label = 'Jugador'

class FormularioEventoFalta(forms.ModelForm):
    partido = FKPartido(queryset=Partido.objects.order_by('fecha'))
    jugador_produjo = FKJugadorPartido(queryset=Jugador_Partido.objects.order_by('jugador'))
    jugador_recibio = FKJugadorPartido(queryset=Jugador_Partido.objects.order_by('jugador'))
    class Meta:
        model = Evento_Falta
        fields = ['partido', 'minu', 'seg', 'jugador_produjo', 'jugador_recibio', 'descripcion']
        labels = {'minu':'Minuto de la falta', 'seg':'Segundo de la falta', 'descripcion':'Descripcion' }
        widget = {'minu':forms.NumberInput(), 'seg':forms.NumberInput(), 'descripcion':forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
            self.fields['partido'].label = 'Partido'
            self.fields['jugador_produjo'].label = 'Jugador que produjo falta'
            self.fields['jugador_recibio'].label = 'Jugador que recibio la falta'

class FormularioOtroEvento(forms.ModelForm):
    partido = FKPartido(queryset=Partido.objects.order_by('fecha'))
    jugador_principal = FKJugadorPartido(queryset=Jugador_Partido.objects.order_by('jugador'))
    class Meta:
        model = Otro_Evento
        fields = ['partido', 'minu', 'seg', 'jugador_principal', 'descripcion']
        labels = {'minu':'Minuto del evento', 'seg':'Segundo del evento', 'descripcion':'Descripcion' }
        widget = {'minu':forms.NumberInput(), 'seg':forms.NumberInput(), 'descripcion':forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields): # Recorremos los campos del modelo
            self.fields[field].widget.attrs.update({
                'class': 'form-control', 'autocomplete': 'off', 'spellcheck':'false'
            })
            self.fields['partido'].label = 'Partido'
            self.fields['jugador_principal'].label = 'Jugador principal del evento'

