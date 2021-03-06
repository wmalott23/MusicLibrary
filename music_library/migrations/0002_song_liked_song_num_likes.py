# Generated by Django 4.0.4 on 2022-04-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='liked',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='num_likes',
            field=models.IntegerField(default=False),
            preserve_default=False,
        ),
    ]
