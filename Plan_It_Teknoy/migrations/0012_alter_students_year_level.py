# Generated by Django 4.1 on 2022-10-30 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plan_It_Teknoy', '0011_alter_users_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='year_level',
            field=models.CharField(default='Not set', max_length=10),
        ),
    ]