# Generated by Django 4.1.3 on 2024-10-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='productId',
            field=models.CharField(default=12345, max_length=20),
            preserve_default=False,
        ),
    ]
