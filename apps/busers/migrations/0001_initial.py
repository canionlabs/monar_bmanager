# Generated by Django 2.1 on 2018-08-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClonedProjects',
            fields=[
                ('token', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('ts', models.DateTimeField(blank=True, null=True)),
                ('json', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cloned_projects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FlashedTokens',
            fields=[
                ('token', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('app_name', models.TextField()),
                ('email', models.TextField(blank=True, null=True)),
                ('project_id', models.IntegerField()),
                ('device_id', models.IntegerField()),
                ('is_activated', models.BooleanField(blank=True, null=True)),
                ('ts', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'flashed_tokens',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ForwardingTokens',
            fields=[
                ('token', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('host', models.TextField()),
                ('email', models.TextField(blank=True, null=True)),
                ('project_id', models.IntegerField(blank=True, null=True)),
                ('device_id', models.IntegerField(blank=True, null=True)),
                ('ts', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Forwarding Token',
                'verbose_name_plural': 'Forwarding Tokens',
                'db_table': 'forwarding_tokens',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('email', models.TextField(primary_key=True, serialize=False)),
                ('reward', models.IntegerField()),
                ('transactionid', models.TextField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('ts', models.DateTimeField()),
            ],
            options={
                'db_table': 'purchase',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Redeem',
            fields=[
                ('token', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('company', models.TextField(blank=True, null=True)),
                ('isredeemed', models.BooleanField(blank=True, null=True)),
                ('reward', models.IntegerField()),
                ('email', models.TextField(blank=True, null=True)),
                ('version', models.IntegerField()),
                ('ts', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'redeem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('email', models.TextField(primary_key=True, serialize=False)),
                ('appname', models.TextField()),
                ('region', models.TextField(blank=True, null=True)),
                ('ip', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('pass_field', models.TextField(blank=True, db_column='pass', null=True)),
                ('last_modified', models.DateTimeField(blank=True, null=True)),
                ('last_logged', models.DateTimeField(blank=True, null=True)),
                ('last_logged_ip', models.TextField(blank=True, null=True)),
                ('is_facebook_user', models.BooleanField(blank=True, null=True)),
                ('is_super_admin', models.BooleanField(blank=True, null=True)),
                ('energy', models.IntegerField(blank=True, null=True)),
                ('json', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Blynk User',
                'verbose_name_plural': 'Blynk Users',
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]