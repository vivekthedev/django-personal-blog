# Generated by Django 3.1.1 on 2021-05-04 19:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210504_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 5, 1, 4, 34, 516736)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]