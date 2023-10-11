# Generated by Django 4.2.5 on 2023-09-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('file', models.FileField(upload_to='file')),
                ('date', models.DateTimeField()),
                ('user', models.CharField(max_length=50)),
                ('is_public', models.BooleanField(default=False)),
                ('album', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
