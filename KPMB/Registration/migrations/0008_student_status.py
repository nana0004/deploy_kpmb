# Generated by Django 4.1.4 on 2022-12-28 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0007_rename_stud_id_student_stud_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default='MP', max_length=3),
        ),
    ]