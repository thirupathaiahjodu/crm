# Generated by Django 4.2.1 on 2023-08-03 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcube', '0023_student_email_student_mobile_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Mobile_Number',
            new_name='mobile_number',
        ),
    ]
