# Generated by Django 4.2 on 2024-02-06 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_shirt_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('zipcode', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='shirt',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.brand'),
        ),
        migrations.AddField(
            model_name='brand',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.address'),
        ),
    ]