# Generated by Django 4.1.2 on 2022-10-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviehere', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='year',
            field=models.DateField(null=True),
        ),
    ]
