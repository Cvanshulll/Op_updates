# Generated by Django 4.2.3 on 2023-09-03 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0004_remove_opportunity_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='op_link',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
