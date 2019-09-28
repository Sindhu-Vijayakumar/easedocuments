# Generated by Django 2.2.5 on 2019-09-27 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documentmanage', '0002_auto_20190927_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='docname',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='username',
        ),
        migrations.AddField(
            model_name='requests',
            name='document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documentmanage.AllDocuments'),
        ),
        migrations.AddField(
            model_name='requests',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]