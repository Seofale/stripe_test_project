# Generated by Django 4.1.1 on 2022-09-16 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_remove_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='currency',
            field=models.CharField(choices=[('usd', 'US dollars'), ('rub', 'RF rubles')], default=None, max_length=3),
            preserve_default=False,
        ),
    ]
