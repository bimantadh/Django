# Generated by Django 4.2.7 on 2023-11-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
