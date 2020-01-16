# Generated by Django 2.2.9 on 2020-01-06 21:39

from django.db import migrations, models
import django.db.models.deletion
import uuid
import wagtail_localize.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtail_localize', '0002_initial_data'),
        ('core', '0011_refactor_accordion_block'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContributorSupportPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('translation_key', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_source_translation', models.BooleanField(default=True)),
                ('locale', models.ForeignKey(default=wagtail_localize.models.default_locale_id, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtail_localize.Locale')),
            ],
            options={
                'abstract': False,
                'unique_together': {('translation_key', 'locale')},
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]