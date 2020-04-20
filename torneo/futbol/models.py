from django.db import models

class RolArbitro(models.Model):
    id = models.AutoField(
        primary_key = True
    )
    nombre = models.CharField(
        max_length = 25
    )
    @classmethod
    def create(cls, id, nombre):
        id = cls(id=id)
        nombre = cls(nombre=nombre)
        return nombre

class Pais(models.Model):
    id = models.IntegerField(
        primary_key = True
    )
    iso = models.CharField(
        max_length = 2,
        null = True
    )
    nombre = models.CharField(
        max_length = 46,
        null = True
    )

class Torneo(models.Model):
    id = models.AutoField(
        primary_key = True
    )
    nombre = models.CharField(
        max_length = 30
    )
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING)

class Ciudad(models.Model):
    codigo = models.AutoField(
        primary_key = True,
    )
    nombre = models.CharField (max_length=40, unique = True)
    poblacion = models.IntegerField ()
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING, default="1")

class Jugador(models.Model):
    codigo = models.IntegerField(
        primary_key = True,
    )
    nombre = models.CharField (max_length= 40, default="1")
    edad = models.CharField(max_length=2, default="1")

class Estadio(models.Model):
    codigo = models.IntegerField(
        primary_key = True,
    )
    nombre = models.CharField (max_length=40)
    id_ciudad = models.ForeignKey(Ciudad,on_delete = models.DO_NOTHING, default="1")
    anno_construccion = models.PositiveSmallIntegerField()
    capacidad = models.IntegerField ()

class Arbitro(models.Model):
    carne = models.IntegerField(
        primary_key = True,
    )
    nombre = models.CharField (max_length=40)
    tutor_de_arbitro = models.ForeignKey('self', on_delete = models.DO_NOTHING, default="1", null = True)
    rol = models.ForeignKey(RolArbitro, on_delete = models.DO_NOTHING, default="1")

class persona_natural(models.Model):
    cedula = models.IntegerField(
        primary_key = True,
    )
    nombre = models.CharField (max_length=40)
    telefono = models.CharField (max_length=20, default="1")

class Equipo(models.Model):
    codigo = models.IntegerField(
        primary_key = True,
    )
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    nombre = models.CharField (max_length=40)
    anno_creacion = models.CharField(max_length=4)
    patrocinador_equipo = models.ForeignKey('self', on_delete = models.CASCADE, default="1", null=True)
    patrocinador_persona_natural = models.ForeignKey(persona_natural, on_delete = models.CASCADE, default="1", null = True)

class Empresa(models.Model):
    codigo = models.IntegerField(
        primary_key = True,
    )
    nombre = models.CharField (max_length=40, unique = True, default="nombre_empresa")
    representante_legal = models.CharField (max_length=40)
    email = models.CharField (max_length=60)
    ciudad_sede_principal = models.ForeignKey(Ciudad, on_delete = models.DO_NOTHING, default="1")
    equipo_patrocinado = models.ForeignKey(Equipo, on_delete = models.DO_NOTHING, default="1", null = True)

class Jugador_Equipo(models.Model):
    equipo_actual = models.ForeignKey(Equipo, on_delete = models.CASCADE, related_name="jugador_equipo_equipo")
    jugador = models.ForeignKey(Jugador, on_delete = models.CASCADE)
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    equipo_anterior = models.ForeignKey(Equipo, on_delete=models.DO_NOTHING, null = True)

class Partido(models.Model):
    arbitro = models.ForeignKey(Arbitro, on_delete = models.CASCADE, default="1")
    estadio = models.ForeignKey(Estadio, on_delete = models.CASCADE, default="1")
    equipo_local = models.ForeignKey(Equipo, on_delete = models.CASCADE, related_name='equipo_local_partido', default="1")
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='equipo_visitante_partido', default="1")
    fecha = models.DateField()
    hora = models.CharField(max_length=5)
    marcador = models.CharField(max_length=10)
    ganador = models.ForeignKey(Equipo, on_delete = models.CASCADE, null = True )
    empate = models.CharField(max_length = 2, default="--", null = True)
    nombre_torneo = models.ForeignKey(Torneo, on_delete=models.DO_NOTHING, default="1")

class Jugador_Partido(models.Model):
    partido = models.ForeignKey(Partido, on_delete = models.CASCADE)
    jugador = models.ForeignKey(Jugador, on_delete = models.CASCADE)
    min_ingreso = models.CharField(
        max_length = 10,
    )
    min_salida = models.CharField(
        max_length = 10,
    )

class Evento_Gol(models.Model):
    partido = models.ForeignKey(Partido, on_delete = models.CASCADE, default="1")
    minu = models.PositiveSmallIntegerField()
    seg = models.PositiveSmallIntegerField()
    Jugador_partido = models.ForeignKey(Jugador_Partido, on_delete = models.CASCADE)

class Evento_Falta(models.Model):
    partido = models.ForeignKey(Partido, on_delete = models.CASCADE)
    minu = models.PositiveSmallIntegerField()
    seg = models.PositiveSmallIntegerField()
    jugador_produjo = models.ForeignKey(Jugador_Partido, on_delete = models.CASCADE, related_name='evento_falta_golpe_jugador_produjo')
    jugador_recibio = models.ForeignKey(Jugador_Partido, on_delete = models.CASCADE, related_name='evento_falta_golpe_jugador_recibido')
    descripcion = models.CharField(max_length=100)

class Otro_Evento(models.Model):
    partido = models.ForeignKey(Partido, on_delete = models.CASCADE)
    minu = models.PositiveSmallIntegerField()
    seg = models.PositiveSmallIntegerField()
    jugador_principal = models.ForeignKey(Jugador_Partido, on_delete=models.DO_NOTHING)
    descripcion = models.CharField(
        max_length=100
    )