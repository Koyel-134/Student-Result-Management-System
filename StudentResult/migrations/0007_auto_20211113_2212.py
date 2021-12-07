# Generated by Django 3.2.6 on 2021-11-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentResult', '0006_auto_20211105_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students3',
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
                ('totalmarks', models.IntegerField(max_length=10)),
                ('percentage', models.IntegerField(max_length=10)),
                ('status', models.CharField(max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Students2',
        ),
    ]
