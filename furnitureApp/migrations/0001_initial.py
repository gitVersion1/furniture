# Generated by Django 4.2.2 on 2023-06-12 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, max_length=60, null=True)),
                ('product_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('product_review', models.TextField(blank=True, max_length=600, null=True)),
                ('product_image', models.ImageField(upload_to='product/')),
            ],
        ),
    ]