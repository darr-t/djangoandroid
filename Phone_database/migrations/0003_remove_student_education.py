# Generated by Django 5.2.1 on 2025-06-04 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Phone_database', '0002_alter_student_education_alter_student_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='education',
        ),
    ]
