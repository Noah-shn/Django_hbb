# Generated by Django 4.0.3 on 2022-04-15 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_graphiccards_products_alter_graphiccards_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphiccards',
            name='Products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.products'),
        ),
    ]
