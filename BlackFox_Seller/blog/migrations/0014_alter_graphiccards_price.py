# Generated by Django 4.0.3 on 2022-04-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_graphiccards_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphiccards',
            name='price',
            field=models.IntegerField(max_length=8),
        ),
    ]
