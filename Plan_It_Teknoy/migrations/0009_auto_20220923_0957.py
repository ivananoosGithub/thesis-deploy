# Generated by Django 3.2.6 on 2022-09-23 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plan_It_Teknoy', '0008_alter_event_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='profile_pic',
            field=models.ImageField(default='Not set', null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='teachers',
            name='profile_pic',
            field=models.ImageField(default='Not set', null=True, upload_to='images'),
        ),
    ]
