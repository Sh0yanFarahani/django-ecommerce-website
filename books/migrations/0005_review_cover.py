# Generated by Django 4.0.10 on 2024-02-06 19:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_rename_another_review_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='cover',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='covers/'),
            preserve_default=False,
        ),
    ]
