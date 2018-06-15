# Generated by Django 2.0 on 2018-06-01 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('his06', '0027_auto_20180601_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientsign',
            old_name='doc_rom',
            new_name='doc_room',
        ),
        migrations.AlterField(
            model_name='patient',
            name='care_id',
            field=models.CharField(db_column='care_id_num', default='20180601873297', error_messages={0: '该诊疗卡号不存在'}, max_length=255, primary_key=True, serialize=False, verbose_name='诊疗卡号'),
        ),
    ]
