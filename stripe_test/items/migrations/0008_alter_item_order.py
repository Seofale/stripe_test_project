# Generated by Django 4.1.1 on 2022-09-15 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_alter_order_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='items', to='items.order'),
        ),
    ]
