# Generated by Django 2.2.4 on 2019-08-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_campaignpage_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignpage',
            name='campaign_id',
            field=models.CharField(blank=True, help_text='Used for analytics and reporting', max_length=255),
        ),
        migrations.AddField(
            model_name='campaignpage',
            name='project',
            field=models.CharField(choices=[('mozillafoundation', 'Mozilla Foundation'), ('thunderbird', 'Thunderbird')], default='mozillafoundation', help_text='The project that donations from this campaign should be associated with', max_length=25),
        ),
        migrations.AddField(
            model_name='landingpage',
            name='campaign_id',
            field=models.CharField(blank=True, help_text='Used for analytics and reporting', max_length=255),
        ),
        migrations.AddField(
            model_name='landingpage',
            name='project',
            field=models.CharField(choices=[('mozillafoundation', 'Mozilla Foundation'), ('thunderbird', 'Thunderbird')], default='mozillafoundation', help_text='The project that donations from this campaign should be associated with', max_length=25),
        ),
    ]