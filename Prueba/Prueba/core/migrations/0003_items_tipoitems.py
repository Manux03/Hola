# Generated by Django 3.2.4 on 2021-07-13 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usuario_usuario_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipoitems',
            fields=[
                ('iditems', models.AutoField(primary_key=True, serialize=False, verbose_name='iditems')),
                ('tipoitems', models.CharField(max_length=50, verbose_name='Tipoitems')),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('iditems', models.AutoField(primary_key=True, serialize=False, verbose_name='iditems')),
                ('nombreitems', models.CharField(max_length=150, verbose_name='nombreitems')),
                ('descripcionitems', models.CharField(max_length=250, verbose_name='descripcionitems')),
                ('subir_imagen', models.ImageField(null=True, upload_to='imagenes')),
                ('tipoitems', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.tipoitems')),
            ],
        ),
    ]
