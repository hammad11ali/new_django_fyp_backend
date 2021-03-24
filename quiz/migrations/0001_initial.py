# Generated by Django 3.1.1 on 2021-03-23 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LearningObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('concept_name', models.CharField(max_length=100)),
                ('action_verb', models.CharField(max_length=100)),
                ('qgenerator', models.FileField(null=True, upload_to='Qgenerators/')),
            ],
        ),
    ]
