# Generated by Django 4.1 on 2022-11-15 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plan_It_Teknoy', '0013_students_students_temp_id_users_users_temp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='students_temp_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='users',
            name='users_temp_id',
            field=models.IntegerField(default=0),
        ),
    ]
