# Generated by Django 2.2.6 on 2019-10-14 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20191014_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': '娘子',
                'verbose_name_plural': '娘子',
                'db_table': 'wife',
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-age', '-id'], 'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
    ]