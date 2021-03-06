# Generated by Django 4.0.3 on 2022-04-13 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphicCards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Nvidia', 'Nvidia'), ('AMD', 'AMD'), ('Intel', 'Intel')], default='GrahicCard', max_length=50)),
                ('title', models.CharField(max_length=35)),
                ('description', models.TextField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('image', models.FileField(blank=True, default='default.jpg', upload_to='')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(choices=[('Monitors', 'Monitors'), ('Graphic Cards', 'Graphic Cards'), ('Cases', 'Cases')], max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Monitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('BenQ', 'BenQ'), ('MSI', 'MSI'), ('AOC', 'AOC'), ('Asus', 'Asus')], max_length=50)),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
                ('image', models.ImageField(default='default.jpg', upload_to='monitors_pics')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GraphicImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='graphiccards_pics')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Products.graphiccards')),
            ],
        ),
    ]
