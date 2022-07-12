# Generated by Django 4.0.5 on 2022-07-12 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_alter_bank_rate_max_alter_bank_rate_min'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='rate_max',
            field=models.FloatField(verbose_name='Ставка, ДО'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='rate_min',
            field=models.FloatField(verbose_name='Ставка, ОТ'),
        ),
    ]
