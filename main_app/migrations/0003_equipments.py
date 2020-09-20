# Generated by Django 2.2.12 on 2020-09-20 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_plans'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=30)),
                ('equipment_price', models.IntegerField()),
                ('unit', models.IntegerField()),
                ('purchased_date', models.DateField()),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]