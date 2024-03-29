# Generated by Django 4.2 on 2024-01-30 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_shirt_brand_shirt_description_shirt_is_bestseller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('brand', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
