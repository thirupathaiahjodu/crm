# Generated by Django 4.2.1 on 2023-06-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vcube', '0013_alter_colabrations_image_alter_courses_name_crsname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recent_placed',
            name='company',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recent_placed',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recent_placed',
            name='pakage',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recent_placed',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
