# Generated by Django 4.0.5 on 2022-07-05 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('floors', '0002_spot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=10)),
                ('vehicle_type', models.CharField(choices=[('car', 'Car'), ('motorcycle', 'Motorcycle')], max_length=10)),
                ('arrived_at', models.DateTimeField(auto_now_add=True)),
                ('paid_at', models.DateTimeField(null=True)),
                ('amount_paid', models.IntegerField(null=True)),
                ('spot', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='floors.spot')),
            ],
        ),
    ]
