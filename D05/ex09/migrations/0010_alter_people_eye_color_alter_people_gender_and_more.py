# Generated by Django 4.2.13 on 2024-07-08 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex09', '0009_alter_people_height_alter_people_mass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='gender',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
