# Generated by Django 3.0.7 on 2022-03-29 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='confirmed',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'Nueva'), ('confirmed', 'Confirmada'), ('paid', 'Pagada'), ('sent', 'Enviada')], default='new', max_length=50, verbose_name='Status'),
        ),
    ]
