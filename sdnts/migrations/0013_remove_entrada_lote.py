# Generated by Django 5.2.1 on 2025-06-12 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdnts', '0012_remove_entrada_nom_entrada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='lote',
        ),
    ]
