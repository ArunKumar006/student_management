# Generated by Django 4.1.7 on 2023-04-04 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_candidate_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='candidate_code',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
