# Generated by Django 4.0.3 on 2022-04-12 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_rename_prce_graphiccards_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphiccards',
            name='image',
            field=models.FileField(default='default.jpg', upload_to='graphiccards_pics'),
        ),
    ]
