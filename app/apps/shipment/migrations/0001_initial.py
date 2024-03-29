# Generated by Django 3.0.7 on 2022-03-29 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0004_auto_20220329_0650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='Dirección')),
                ('status', models.CharField(choices=[('new', 'Nuevo'), ('sent', 'Enviado'), ('delivered', 'Entregado')], max_length=50, verbose_name='Estatus')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order', verbose_name='Pedido')),
            ],
        ),
    ]
