# Generated by Django 4.0.3 on 2022-04-17 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0020_remove_sell_sell_products_sell_sell_products_cards_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='sell_products_cards',
            field=models.OneToOneField(default='Sell', on_delete=django.db.models.deletion.CASCADE, to='Products.monitors'),
        ),
    ]