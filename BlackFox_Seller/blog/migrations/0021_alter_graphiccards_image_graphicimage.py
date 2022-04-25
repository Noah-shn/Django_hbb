# Generated by Django 4.0.3 on 2022-04-12 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_graphiccards_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphiccards',
            name='image',
            field=models.FileField(blank=True, default='default.jpg', upload_to=''),
        ),
        migrations.CreateModel(
            name='GraphicImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='graphiccards_pics')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.graphiccards')),
            ],
        ),
    ]
