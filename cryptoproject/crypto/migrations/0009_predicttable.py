# Generated by Django 4.0.1 on 2022-02-16 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0008_delete_testtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='predicttable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Crypto_Name', models.CharField(max_length=255, verbose_name='Crypto Name')),
                ('Price', models.CharField(max_length=255, verbose_name='Price')),
                ('Marketcap', models.CharField(max_length=255, verbose_name='Market Cap')),
            ],
        ),
    ]
