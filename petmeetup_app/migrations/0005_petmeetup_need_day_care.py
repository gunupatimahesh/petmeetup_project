# Generated by Django 5.0.2 on 2024-02-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petmeetup_app', '0004_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='petmeetup',
            name='need_day_care',
            field=models.BooleanField(default=False),
        ),
    ]
