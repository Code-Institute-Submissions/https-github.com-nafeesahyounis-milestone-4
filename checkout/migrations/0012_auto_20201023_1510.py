# Generated by Django 3.0.9 on 2020-10-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_remove_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=6),
        ),
    ]