# Generated by Django 4.0.3 on 2022-04-12 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_graphiccards_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graphiccards',
            name='price',
        ),
    ]
