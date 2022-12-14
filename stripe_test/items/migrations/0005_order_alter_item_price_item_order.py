# Generated by Django 4.1.1 on 2022-09-15 13:08

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_item_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='items', to='items.order'),
            preserve_default=False,
        ),
    ]
