# Generated by Django 4.0.3 on 2022-04-12 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_rename_p_author_graphiccards_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphiccards',
            name='price',
            field=models.IntegerField(default='DZD', max_length=8),
        ),
    ]
