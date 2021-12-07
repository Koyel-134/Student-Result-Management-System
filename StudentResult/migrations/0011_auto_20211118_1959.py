# Generated by Django 3.2.6 on 2021-11-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentResult', '0010_auto_20211118_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('fullname', models.CharField(max_length=50)),
                ('psw', models.CharField(max_length=10)),
                ('oldpsw', models.CharField(max_length=10)),
                ('newpsw', models.CharField(max_length=10)),
                ('pswrepeat', models.CharField(max_length=10)),
                ('designation', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('phone', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Teachers5',
        ),
    ]