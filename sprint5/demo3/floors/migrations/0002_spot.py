# Generated by Django 4.0.5 on 2022-06-29 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('floors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety', models.CharField(choices=[('car', 'Car'), ('motorcycle', 'Motorcycle')], default='car', max_length=127)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spots', to='floors.floor')),
            ],
        ),
    ]
