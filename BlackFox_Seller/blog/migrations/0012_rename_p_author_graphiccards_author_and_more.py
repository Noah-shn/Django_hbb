# Generated by Django 4.0.3 on 2022-04-10 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_graphiccards_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graphiccards',
            old_name='p_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='graphiccards',
            old_name='p_descript',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='graphiccards',
            old_name='p_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='graphiccards',
            old_name='p_name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='monitors',
            old_name='m_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='monitors',
            old_name='m_descript',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='monitors',
            old_name='m_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='monitors',
            old_name='m_brand',
            new_name='title',
        ),
    ]
