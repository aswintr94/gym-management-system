# Generated by Django 2.2.12 on 2020-09-20 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_equipments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('plan', models.CharField(max_length=20)),
                ('joining_date', models.DateField()),
                ('plan_expiry_date', models.DateField()),
                ('initial_amount', models.IntegerField()),
            ],
        ),
    ]
