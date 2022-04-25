# Generated by Django 4.0.3 on 2022-04-21 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangoJS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='serie',
            field=models.CharField(choices=[('Rtx 3060ti', 'Rtx 3060ti'), ('5700xt', '5700xt'), ('A380', 'A380')], default='Card', max_length=12),
        ),
        migrations.AlterField(
            model_name='produit',
            name='choix',
            field=models.ForeignKey(choices=[('Nvidia', 'Nvidia'), ('AMD', 'AMD'), ('intel', 'intel')], on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
