# Generated by Django 4.0.4 on 2022-06-29 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot_api', '0005_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contact_telephone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Контактный телефон'),
        ),
        migrations.AlterField(
            model_name='order',
            name='execution_status',
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Статус выполнения заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_items',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Товары из заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay_status',
            field=models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Статус оплаты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='result_orders_price',
            field=models.FloatField(blank=True, default=0, verbose_name='Итоговая цена заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_api.botusers', verbose_name='Пользователь'),
        ),
    ]
