# Generated by Django 5.0.8 on 2024-08-12 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.product'),
        ),
    ]
