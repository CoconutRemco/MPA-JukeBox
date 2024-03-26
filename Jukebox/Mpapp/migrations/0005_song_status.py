# Generated by Django 5.0.3 on 2024-03-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mpapp', '0004_alter_genre_managers_alter_playlist_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
