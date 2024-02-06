# Generated by Django 4.0.10 on 2024-02-06 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_review_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='cover',
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]