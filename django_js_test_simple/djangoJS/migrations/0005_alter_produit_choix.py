# Generated by Django 4.0.3 on 2022-04-24 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangoJS', '0004_alter_produit_choix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='choix',
            field=models.ForeignKey(choices=[(None, 'Nvidia'), ('AMD', 'AMD'), ('intel', 'intel')], on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]