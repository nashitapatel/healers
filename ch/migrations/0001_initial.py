# Generated by Django 3.0.4 on 2023-01-14 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chathistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=20)),
                ('answer', models.CharField(max_length=100)),
                ('conversation_time', models.DateTimeField()),
            ],
        ),
    ]
