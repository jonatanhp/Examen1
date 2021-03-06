# Generated by Django 3.2.9 on 2021-11-03 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_created=True)),
                ('marca', models.CharField(max_length=100)),
                ('serie', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('disponible', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
    ]
