# Generated by Django 4.2.13 on 2024-07-08 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex09', '0007_alter_people_homeworld'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='birth_year',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
