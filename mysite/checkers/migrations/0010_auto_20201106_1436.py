# Generated by Django 3.1.1 on 2020-11-06 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkers', '0009_auto_20201106_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game_session',
            name='id',
        ),
        migrations.AlterField(
            model_name='game_session',
            name='game_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]