# Generated by Django 4.2.1 on 2023-05-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_blogconfiguration_show_post_header_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogconfiguration',
            name='auto_approve_comments',
            field=models.BooleanField(blank=True, default=False, verbose_name='Aprovar comentários automaticamente'),
        ),
        migrations.AddField(
            model_name='blogconfiguration',
            name='show_comments',
            field=models.BooleanField(blank=True, default=True, verbose_name='Mostrar comentários'),
        ),
        migrations.AlterField(
            model_name='blogconfiguration',
            name='show_post_header',
            field=models.BooleanField(blank=True, default=True, verbose_name='Mostrar header do post'),
        ),
        migrations.AlterField(
            model_name='blogconfiguration',
            name='show_post_image',
            field=models.BooleanField(blank=True, default=True, verbose_name='Mostrar imagem do post'),
        ),
    ]