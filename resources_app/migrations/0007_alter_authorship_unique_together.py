# Generated by Django 4.2.6 on 2023-11-19 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources_app', '0006_authorship'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='authorship',
            unique_together={('paper', 'author')},
        ),
    ]