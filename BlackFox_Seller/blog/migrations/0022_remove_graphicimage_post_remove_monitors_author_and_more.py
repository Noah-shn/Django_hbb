# Generated by Django 4.0.3 on 2022-04-13 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_alter_graphiccards_image_graphicimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graphicimage',
            name='post',
        ),
        migrations.RemoveField(
            model_name='monitors',
            name='author',
        ),
        migrations.DeleteModel(
            name='GraphicCards',
        ),
        migrations.DeleteModel(
            name='GraphicImage',
        ),
        migrations.DeleteModel(
            name='Monitors',
        ),
    ]
