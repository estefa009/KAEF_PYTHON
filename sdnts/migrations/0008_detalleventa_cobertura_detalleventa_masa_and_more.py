# Generated by Django 5.2.2 on 2025-06-11 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdnts', '0007_detalleventa_fecha_entrega'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='cobertura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sdnts.glaseado'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='masa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sdnts.sabormasa'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='topping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sdnts.topping'),
        ),
    ]
