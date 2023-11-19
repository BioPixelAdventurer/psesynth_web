# Generated by Django 4.2.6 on 2023-11-19 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources_app', '0005_year_papertemp_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources_app.author')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources_app.papertemp')),
            ],
        ),
    ]