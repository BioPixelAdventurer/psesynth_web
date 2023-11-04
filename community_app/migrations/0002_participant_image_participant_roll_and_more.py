# Generated by Django 4.2.6 on 2023-10-31 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='image',
            field=models.ImageField(default='psesyn_app/static/psesyn/images/community/default.png', upload_to='participants/'),
        ),
        migrations.AddField(
            model_name='participant',
            name='roll',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='participant',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='participant',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
