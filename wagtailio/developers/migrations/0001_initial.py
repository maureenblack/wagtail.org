# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 13:11
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0028_merge"),
        ("images", "0004_auto_20160727_1108"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="DevelopersPage",
                    fields=[
                        (
                            "page_ptr",
                            models.OneToOneField(
                                auto_created=True,
                                on_delete=django.db.models.deletion.CASCADE,
                                parent_link=True,
                                primary_key=True,
                                serialize=False,
                                to="wagtailcore.Page",
                            ),
                        ),
                        (
                            "social_text",
                            models.CharField(
                                blank=True,
                                help_text="Description of this page as it should appear when shared on social networks, or in Google results",
                                max_length=255,
                                verbose_name="Meta description",
                            ),
                        ),
                        (
                            "listing_intro",
                            models.TextField(
                                blank=True,
                                help_text="Summary of this page to display when this is linked from elsewhere in the site.",
                            ),
                        ),
                        ("introduction", models.CharField(max_length=255)),
                        ("body_heading", models.CharField(max_length=255)),
                        ("body", wagtail.fields.RichTextField(blank=True)),
                        (
                            "listing_image",
                            models.ForeignKey(
                                blank=True,
                                help_text="Image to display along with summary, when this page is linked from elsewhere in the site.",
                                null=True,
                                on_delete=django.db.models.deletion.SET_NULL,
                                related_name="+",
                                to="images.WagtailIOImage",
                            ),
                        ),
                        (
                            "social_image",
                            models.ForeignKey(
                                blank=True,
                                help_text="Image to appear alongside 'Meta descro[topm', particularly for sharing on social networks",
                                null=True,
                                on_delete=django.db.models.deletion.SET_NULL,
                                related_name="+",
                                to="images.WagtailIOImage",
                                verbose_name="Meta image",
                            ),
                        ),
                    ],
                    options={
                        "db_table": "core_developerspage",
                    },
                    bases=("wagtailcore.page", models.Model),
                ),
                migrations.CreateModel(
                    name="DevelopersPageOptions",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        (
                            "sort_order",
                            models.IntegerField(blank=True, editable=False, null=True),
                        ),
                        (
                            "icon",
                            models.CharField(
                                choices=[
                                    ("fa-github", "Github"),
                                    ("fa-google", "Google"),
                                    ("fa-eye", "Eye"),
                                    ("fa-server", "Servers"),
                                ],
                                max_length=255,
                            ),
                        ),
                        ("title", models.CharField(max_length=255)),
                        ("summary", models.CharField(max_length=255)),
                        (
                            "external_link",
                            models.URLField(blank=True, verbose_name="External link"),
                        ),
                        (
                            "internal_link",
                            models.ForeignKey(
                                blank=True,
                                null=True,
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="+",
                                to="wagtailcore.Page",
                            ),
                        ),
                        (
                            "page",
                            modelcluster.fields.ParentalKey(
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="options",
                                to="developers.DevelopersPage",
                            ),
                        ),
                    ],
                    options={
                        "db_table": "core_developerspageoptions",
                    },
                ),
            ],
            database_operations=[],
        ),
    ]
