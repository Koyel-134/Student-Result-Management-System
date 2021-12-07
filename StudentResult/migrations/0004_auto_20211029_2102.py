# Generated by Django 3.2.6 on 2021-10-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentResult', '0003_auto_20211009_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students2',
            fields=[
                ('enroll', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=10)),
                ('semester', models.IntegerField(max_length=10)),
                ('toc', models.IntegerField(max_length=10)),
                ('dbms', models.IntegerField(max_length=10)),
                ('departmentalelectives', models.IntegerField(max_length=10)),
                ('openelectives', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]
