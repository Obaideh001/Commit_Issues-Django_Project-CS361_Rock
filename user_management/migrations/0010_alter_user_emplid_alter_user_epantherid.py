# Generated by Django 5.0.4 on 2024-05-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0009_alter_user_emplid_alter_user_epantherid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='emplid',
            field=models.CharField(max_length=10, unique=True, verbose_name='emplid'),
        ),
        migrations.AlterField(
            model_name='user',
            name='epantherid',
            field=models.CharField(max_length=20, unique=True, verbose_name='ePanther ID'),
        ),
    ]
