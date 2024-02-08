# Generated by Django 5.0.1 on 2024-02-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hw2', '0003_product_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='count',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='count',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='app_hw2.OrderItem', to='app_hw2.product'),
        ),
        migrations.AlterField(
            model_name='client',
            name='register_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='added_date',
            field=models.DateTimeField(),
        ),
    ]
