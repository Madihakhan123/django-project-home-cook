# Generated by Django 3.2 on 2021-11-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_remove_order_itemsjson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
