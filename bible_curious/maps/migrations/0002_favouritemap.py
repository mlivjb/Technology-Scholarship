# Generated by Django 5.0.6 on 2024-09-07 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_sub', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
