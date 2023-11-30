# Generated by Django 4.2.1 on 2023-08-04 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vcube', '0027_delete_placedstudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='newstudent',
            name='Graduation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='newstudent',
            name='Gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vcube.gender'),
        ),
    ]