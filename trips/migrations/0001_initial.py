# Generated by Django 2.2.5 on 2019-11-09 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicles', '0001_initial'),
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_date', models.DateField(verbose_name='Trip date')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_destinations', to='places.Place', verbose_name='To')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_origins', to='places.Place', verbose_name='From')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to=settings.AUTH_USER_MODEL, verbose_name='Driver')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_vehicles', to='vehicles.Vehicle', verbose_name='Vehicle')),
            ],
            options={
                'verbose_name': 'Trip',
                'verbose_name_plural': 'Trips',
            },
        ),
    ]
