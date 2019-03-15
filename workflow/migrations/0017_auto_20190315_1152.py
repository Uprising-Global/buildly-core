# Generated by Django 2.0.7 on 2019-03-15 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0016_populate_wf2_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalworkflowlevel2',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='workflowlevel2',
            name='created_by',
        ),
        migrations.RenameField(
            model_name='historicalworkflowlevel2',
            old_name='_created_by',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='workflowlevel2',
            old_name='_created_by',
            new_name='created_by',
        ),
    ]
