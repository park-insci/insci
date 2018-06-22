# Generated by Django 2.0.6 on 2018-06-20 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20180618_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='категория')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(max_length=100, verbose_name='краткое описание'),
        ),
    ]
