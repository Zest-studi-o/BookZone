# Generated by Django 3.2.24 on 2024-03-03 13:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20240303_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='wishlist',
            field=models.ManyToManyField(blank=True, related_name='wishlist_item', to=settings.AUTH_USER_MODEL),
        ),
    ]