# Generated by Django 4.1.4 on 2022-12-28 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0005_rename_phone_student_phone_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='phone_no',
            new_name='phone_No',
        ),
    ]
