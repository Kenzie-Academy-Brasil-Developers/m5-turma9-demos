# Generated by Django 4.0.5 on 2022-07-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='amount_paid',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='paid_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
