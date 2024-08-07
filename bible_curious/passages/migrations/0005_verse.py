# Generated by Django 5.0.6 on 2024-07-28 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passages', '0004_step_step_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading', models.CharField(max_length=50)),
                ('verse', models.TextField()),
                ('explanation', models.TextField()),
                ('group', models.CharField(max_length=50)),
                ('week', models.IntegerField()),
            ],
        ),
    ]
