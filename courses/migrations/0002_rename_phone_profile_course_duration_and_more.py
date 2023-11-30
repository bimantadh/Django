# Generated by Django 4.2.7 on 2023-11-30 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone',
            new_name='course_duration',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='course_id',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='last_name',
            new_name='course_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.AddField(
            model_name='profile',
            name='course_details',
            field=models.CharField(default='science', max_length=10000),
            preserve_default=False,
        ),
    ]