# Generated by Django 2.2.9 on 2020-01-09 15:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload',
            field=models.ImageField(null=True, upload_to='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date de publication'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date de publication'),
        ),
        migrations.AlterField(
            model_name='post',
            name='texte',
            field=models.TextField(verbose_name='texte'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titre'),
        ),
    ]