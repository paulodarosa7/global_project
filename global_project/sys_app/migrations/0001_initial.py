# Generated by Django 5.2 on 2025-04-23 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(max_length=100)),
                ('data_ida', models.DateField()),
                ('data_volta', models.DateField()),
            ],
        ),
    ]
