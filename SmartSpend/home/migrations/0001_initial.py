# Generated by Django 4.1.6 on 2023-02-13 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenseName', models.TextField(default='abc', max_length=30)),
                ('expenseAmount', models.IntegerField(default='0000000')),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]
