# Generated by Django 4.0.5 on 2022-06-26 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_delete_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='word_length',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
