# Generated by Django 4.2.1 on 2023-06-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcube', '0007_colabrations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recent_Placed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
