# Generated by Django 5.1.4 on 2025-01-20 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainer',
            old_name='birth_date',
            new_name='bith_date',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('A', 'Agua'), ('L', 'Lagartija'), ('T', 'Tierra'), ('P', 'Planta'), ('E', 'Eléctrico'), ('F', 'Fuego')], max_length=30),
        ),
    ]
