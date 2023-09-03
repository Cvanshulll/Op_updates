# Generated by Django 4.2.3 on 2023-09-03 05:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_rename_recipe_opportunity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunity',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='instructions',
        ),
        migrations.AddField(
            model_name='opportunity',
            name='batch',
            field=models.CharField(default=2.2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opportunity',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opportunity',
            name='op_link',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opportunity',
            name='role',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opportunity',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]