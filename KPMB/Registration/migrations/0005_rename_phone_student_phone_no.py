# Generated by Django 4.1.4 on 2022-12-28 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0004_rename_id_student_stud_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='phone',
            new_name='phone_no',
        ),
    ]