# Generated by Django 2.2.11 on 2020-04-19 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('futbol', '0002_auto_20200419_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbitro',
            name='rol',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='futbol.RolArbitro'),
        ),
        migrations.AlterField(
            model_name='arbitro',
            name='tutor_de_arbitro',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='futbol.Arbitro'),
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='codigo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='ciudad_sede_principal',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='futbol.Ciudad'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='equipo_patrocinado',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='futbol.Equipo'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='patrocinador_equipo',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='futbol.Equipo'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='patrocinador_persona_natural',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='futbol.persona_natural'),
        ),
        migrations.AlterField(
            model_name='jugador_equipo',
            name='equipo_actual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugador_equipo_equipo', to='futbol.Equipo'),
        ),
        migrations.AlterField(
            model_name='jugador_equipo',
            name='equipo_anterior',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='futbol.Equipo'),
        ),
        migrations.AlterField(
            model_name='jugador_equipo',
            name='jugador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbol.Jugador'),
        ),
        migrations.AlterField(
            model_name='torneo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
