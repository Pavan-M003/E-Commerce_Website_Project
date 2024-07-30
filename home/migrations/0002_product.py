# Generated by Django 5.0.7 on 2024-07-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=122)),
                ('price', models.FloatField()),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
