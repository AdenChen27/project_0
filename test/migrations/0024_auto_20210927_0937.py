# Generated by Django 3.2.6 on 2021-09-27 09:37

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0023_lemma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lemma',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='passage',
            name='tags',
            field=django_mysql.models.ListCharField(models.CharField(max_length=20), default='', max_length=105, size=5),
        ),
        migrations.AlterField(
            model_name='word',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='worddef',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='wordfreq',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
