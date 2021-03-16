# Generated by Django 3.0.8 on 2020-07-12 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_delete_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('G', 'No Category'), ('F', 'Fashion'), ('S', 'Sport'), ('T', 'Toy'), ('C', 'Car')], default='G', max_length=1),
        ),
    ]