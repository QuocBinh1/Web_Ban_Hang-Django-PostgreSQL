# Generated by Django 5.0.1 on 2024-05-28 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payments',
            field=models.CharField(choices=[('cod', 'COD'), ('bank transfer', 'Bank Transfer')], default='COD', max_length=50),
        ),
    ]
