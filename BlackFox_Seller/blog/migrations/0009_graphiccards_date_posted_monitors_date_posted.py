# Generated by Django 4.0.3 on 2022-04-08 12:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_graphiccards_monitors_delete_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphiccards',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='monitors',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
