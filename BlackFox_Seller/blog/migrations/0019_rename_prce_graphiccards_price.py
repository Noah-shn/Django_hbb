# Generated by Django 4.0.3 on 2022-04-12 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_graphiccards_prce'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graphiccards',
            old_name='prce',
            new_name='price',
        ),
    ]
