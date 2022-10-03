# Generated by Django 3.2.12 on 2022-09-02 14:38

import django.db.models.deletion
from django.db import migrations, models

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks

import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailmedia", "0004_duration_optional_floatfield"),
        ("core", "0050_update_templates"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="autoplay_video",
            field=models.BooleanField(
                default=False,
                help_text="Automatically start the video when the video and page loads.The video will start over again, every time it is finished",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="call_to_action",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "cta",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.core.blocks.CharBlock(
                                        label="CTA text", max_length=255, required=False
                                    ),
                                ),
                                (
                                    "cta_page",
                                    wagtail.core.blocks.PageChooserBlock(
                                        label="CTA page", required=False
                                    ),
                                ),
                                (
                                    "cta_url",
                                    wagtail.core.blocks.URLBlock(
                                        label="CTA URL", required=False
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                help_text="Allows for a maximum of 2 CTA blocks",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="code_snippet",
            field=models.TextField(blank=True, default="pip install wagtail"),
        ),
        migrations.AddField(
            model_name="homepage",
            name="heading",
            field=models.TextField(blank=True, verbose_name="Heading"),
        ),
        migrations.AddField(
            model_name="homepage",
            name="icon",
            field=models.CharField(
                blank=True,
                choices=[
                    ("arrow-alt", "Arrow alt"),
                    ("arrow-in-circle", "Arrow in circle"),
                    ("arrow-in-square", "Arrow in square"),
                    ("arrows", "Arrows"),
                    ("blog", "Blog"),
                    ("bread", "Bread"),
                    ("briefcase", "Briefcase"),
                    ("building", "Building"),
                    ("calendar", "Calendar"),
                    ("code-file", "Code File"),
                    ("document", "Document"),
                    ("envelope", "Envelope"),
                    ("explanation", "Explanation"),
                    ("eye", "Eye"),
                    ("flame", "Flame"),
                    ("friends", "Friends"),
                    ("github", "Github"),
                    ("handshake", "Handshake"),
                    ("heart", "Heart"),
                    ("history", "History"),
                    ("id-card", "ID Card"),
                    ("image", "Image"),
                    ("knife-fork", "Knife Fork"),
                    ("leaf", "Leaf"),
                    ("location-pin", "Location Pin"),
                    ("map", "Map"),
                    ("magnifying-glass", "Magnifying Glass"),
                    ("money", "Money"),
                    ("moon", "Moon"),
                    ("one-two-steps", "One Two Steps"),
                    ("padlock", "Padlock"),
                    ("paper-plane", "Paper Plane"),
                    ("paper-stack", "Paper Stack"),
                    ("pen-checkbox", "Pen Checkbox"),
                    ("person-in-tie", "Person in Tie"),
                    ("python", "Python"),
                    ("question-mark-circle", "Question Mark Circle"),
                    ("quotes", "Quotes"),
                    ("release-cycle", "Release Cycle"),
                    ("roadmap", "Roadmap"),
                    ("rocket", "Rocket"),
                    ("rollback", "Rollback"),
                    ("slack", "Slack"),
                    ("speech-bubble", "Speech Bubble"),
                    ("sun-cloud", "Sun Cloud"),
                    ("table-tennis", "Table Tennis"),
                    ("tree", "Tree"),
                    ("wordpress", "Wordpress"),
                    ("world", "World"),
                ],
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="intro",
            field=wagtail.core.fields.RichTextField(blank=True, verbose_name="Intro"),
        ),
        migrations.AddField(
            model_name="homepage",
            name="sub_heading",
            field=models.TextField(blank=True, verbose_name="Sub heading"),
        ),
        migrations.AddField(
            model_name="homepage",
            name="video",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailmedia.media",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "get_started_block",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            "core.GetStartedSnippet", icon="th-list"
                        ),
                    ),
                    (
                        "headline",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.core.blocks.CharBlock(max_length=255),
                                ),
                                (
                                    "sub_heading",
                                    wagtail.core.blocks.TextBlock(required=False),
                                ),
                                (
                                    "intro",
                                    wagtail.core.blocks.TextBlock(required=False),
                                ),
                                (
                                    "cta",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "text",
                                                wagtail.core.blocks.CharBlock(
                                                    label="CTA text",
                                                    max_length=255,
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "cta_page",
                                                wagtail.core.blocks.PageChooserBlock(
                                                    label="CTA page", required=False
                                                ),
                                            ),
                                            (
                                                "cta_url",
                                                wagtail.core.blocks.URLBlock(
                                                    label="CTA URL", required=False
                                                ),
                                            ),
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    "icon",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("arrow-alt", "Arrow alt"),
                                            ("arrow-in-circle", "Arrow in circle"),
                                            ("arrow-in-square", "Arrow in square"),
                                            ("arrows", "Arrows"),
                                            ("blog", "Blog"),
                                            ("bread", "Bread"),
                                            ("briefcase", "Briefcase"),
                                            ("building", "Building"),
                                            ("calendar", "Calendar"),
                                            ("code-file", "Code File"),
                                            ("document", "Document"),
                                            ("envelope", "Envelope"),
                                            ("explanation", "Explanation"),
                                            ("eye", "Eye"),
                                            ("flame", "Flame"),
                                            ("friends", "Friends"),
                                            ("github", "Github"),
                                            ("handshake", "Handshake"),
                                            ("heart", "Heart"),
                                            ("history", "History"),
                                            ("id-card", "ID Card"),
                                            ("image", "Image"),
                                            ("knife-fork", "Knife Fork"),
                                            ("leaf", "Leaf"),
                                            ("location-pin", "Location Pin"),
                                            ("map", "Map"),
                                            ("magnifying-glass", "Magnifying Glass"),
                                            ("money", "Money"),
                                            ("moon", "Moon"),
                                            ("one-two-steps", "One Two Steps"),
                                            ("padlock", "Padlock"),
                                            ("paper-plane", "Paper Plane"),
                                            ("paper-stack", "Paper Stack"),
                                            ("pen-checkbox", "Pen Checkbox"),
                                            ("person-in-tie", "Person in Tie"),
                                            ("python", "Python"),
                                            (
                                                "question-mark-circle",
                                                "Question Mark Circle",
                                            ),
                                            ("quotes", "Quotes"),
                                            ("release-cycle", "Release Cycle"),
                                            ("roadmap", "Roadmap"),
                                            ("rocket", "Rocket"),
                                            ("rollback", "Rollback"),
                                            ("slack", "Slack"),
                                            ("speech-bubble", "Speech Bubble"),
                                            ("sun-cloud", "Sun Cloud"),
                                            ("table-tennis", "Table Tennis"),
                                            ("tree", "Tree"),
                                            ("wordpress", "Wordpress"),
                                            ("world", "World"),
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    "dark_background",
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "highlight",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.core.blocks.CharBlock(max_length=100),
                                ),
                                (
                                    "description",
                                    wagtail.core.blocks.TextBlock(required=False),
                                ),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "image_on_right",
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                (
                                    "meta_text",
                                    wagtail.core.blocks.CharBlock(
                                        max_length=50, required=False
                                    ),
                                ),
                                (
                                    "meta_icon",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("arrow-alt", "Arrow alt"),
                                            ("arrow-in-circle", "Arrow in circle"),
                                            ("arrow-in-square", "Arrow in square"),
                                            ("arrows", "Arrows"),
                                            ("blog", "Blog"),
                                            ("bread", "Bread"),
                                            ("briefcase", "Briefcase"),
                                            ("building", "Building"),
                                            ("calendar", "Calendar"),
                                            ("code-file", "Code File"),
                                            ("document", "Document"),
                                            ("envelope", "Envelope"),
                                            ("explanation", "Explanation"),
                                            ("eye", "Eye"),
                                            ("flame", "Flame"),
                                            ("friends", "Friends"),
                                            ("github", "Github"),
                                            ("handshake", "Handshake"),
                                            ("heart", "Heart"),
                                            ("history", "History"),
                                            ("id-card", "ID Card"),
                                            ("image", "Image"),
                                            ("knife-fork", "Knife Fork"),
                                            ("leaf", "Leaf"),
                                            ("location-pin", "Location Pin"),
                                            ("map", "Map"),
                                            ("magnifying-glass", "Magnifying Glass"),
                                            ("money", "Money"),
                                            ("moon", "Moon"),
                                            ("one-two-steps", "One Two Steps"),
                                            ("padlock", "Padlock"),
                                            ("paper-plane", "Paper Plane"),
                                            ("paper-stack", "Paper Stack"),
                                            ("pen-checkbox", "Pen Checkbox"),
                                            ("person-in-tie", "Person in Tie"),
                                            ("python", "Python"),
                                            (
                                                "question-mark-circle",
                                                "Question Mark Circle",
                                            ),
                                            ("quotes", "Quotes"),
                                            ("release-cycle", "Release Cycle"),
                                            ("roadmap", "Roadmap"),
                                            ("rocket", "Rocket"),
                                            ("rollback", "Rollback"),
                                            ("slack", "Slack"),
                                            ("speech-bubble", "Speech Bubble"),
                                            ("sun-cloud", "Sun Cloud"),
                                            ("table-tennis", "Table Tennis"),
                                            ("tree", "Tree"),
                                            ("wordpress", "Wordpress"),
                                            ("world", "World"),
                                        ],
                                        required=False,
                                    ),
                                ),
                                (
                                    "cta",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "text",
                                                wagtail.core.blocks.CharBlock(
                                                    label="CTA text",
                                                    max_length=255,
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "cta_page",
                                                wagtail.core.blocks.PageChooserBlock(
                                                    label="CTA page", required=False
                                                ),
                                            ),
                                            (
                                                "cta_url",
                                                wagtail.core.blocks.URLBlock(
                                                    label="CTA URL", required=False
                                                ),
                                            ),
                                        ],
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "icon_bullets",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "icon_bullets",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "icon",
                                                    wagtail.core.blocks.ChoiceBlock(
                                                        choices=[
                                                            ("arrow-alt", "Arrow alt"),
                                                            (
                                                                "arrow-in-circle",
                                                                "Arrow in circle",
                                                            ),
                                                            (
                                                                "arrow-in-square",
                                                                "Arrow in square",
                                                            ),
                                                            ("arrows", "Arrows"),
                                                            ("blog", "Blog"),
                                                            ("bread", "Bread"),
                                                            ("briefcase", "Briefcase"),
                                                            ("building", "Building"),
                                                            ("calendar", "Calendar"),
                                                            ("code-file", "Code File"),
                                                            ("document", "Document"),
                                                            ("envelope", "Envelope"),
                                                            (
                                                                "explanation",
                                                                "Explanation",
                                                            ),
                                                            ("eye", "Eye"),
                                                            ("flame", "Flame"),
                                                            ("friends", "Friends"),
                                                            ("github", "Github"),
                                                            ("handshake", "Handshake"),
                                                            ("heart", "Heart"),
                                                            ("history", "History"),
                                                            ("id-card", "ID Card"),
                                                            ("image", "Image"),
                                                            (
                                                                "knife-fork",
                                                                "Knife Fork",
                                                            ),
                                                            ("leaf", "Leaf"),
                                                            (
                                                                "location-pin",
                                                                "Location Pin",
                                                            ),
                                                            ("map", "Map"),
                                                            (
                                                                "magnifying-glass",
                                                                "Magnifying Glass",
                                                            ),
                                                            ("money", "Money"),
                                                            ("moon", "Moon"),
                                                            (
                                                                "one-two-steps",
                                                                "One Two Steps",
                                                            ),
                                                            ("padlock", "Padlock"),
                                                            (
                                                                "paper-plane",
                                                                "Paper Plane",
                                                            ),
                                                            (
                                                                "paper-stack",
                                                                "Paper Stack",
                                                            ),
                                                            (
                                                                "pen-checkbox",
                                                                "Pen Checkbox",
                                                            ),
                                                            (
                                                                "person-in-tie",
                                                                "Person in Tie",
                                                            ),
                                                            ("python", "Python"),
                                                            (
                                                                "question-mark-circle",
                                                                "Question Mark Circle",
                                                            ),
                                                            ("quotes", "Quotes"),
                                                            (
                                                                "release-cycle",
                                                                "Release Cycle",
                                                            ),
                                                            ("roadmap", "Roadmap"),
                                                            ("rocket", "Rocket"),
                                                            ("rollback", "Rollback"),
                                                            ("slack", "Slack"),
                                                            (
                                                                "speech-bubble",
                                                                "Speech Bubble",
                                                            ),
                                                            ("sun-cloud", "Sun Cloud"),
                                                            (
                                                                "table-tennis",
                                                                "Table Tennis",
                                                            ),
                                                            ("tree", "Tree"),
                                                            ("wordpress", "Wordpress"),
                                                            ("world", "World"),
                                                        ]
                                                    ),
                                                ),
                                                (
                                                    "heading",
                                                    wagtail.core.blocks.CharBlock(
                                                        max_length=255
                                                    ),
                                                ),
                                                (
                                                    "description",
                                                    wagtail.core.blocks.RichTextBlock(
                                                        features=[
                                                            "bold",
                                                            "italic",
                                                            "link",
                                                        ],
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "cta",
                                                    wagtail.core.blocks.StructBlock(
                                                        [
                                                            (
                                                                "text",
                                                                wagtail.core.blocks.CharBlock(
                                                                    label="CTA text",
                                                                    max_length=255,
                                                                    required=False,
                                                                ),
                                                            ),
                                                            (
                                                                "cta_page",
                                                                wagtail.core.blocks.PageChooserBlock(
                                                                    label="CTA page",
                                                                    required=False,
                                                                ),
                                                            ),
                                                            (
                                                                "cta_url",
                                                                wagtail.core.blocks.URLBlock(
                                                                    label="CTA URL",
                                                                    required=False,
                                                                ),
                                                            ),
                                                        ],
                                                        required=False,
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                )
                            ],
                            icon="list-alt",
                        ),
                    ),
                    (
                        "logos",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "logos",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.images.blocks.ImageChooserBlock()
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "multiple_quotes",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.core.blocks.TextBlock(required=True),
                                ),
                                (
                                    "quotes",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "quote",
                                                    wagtail.core.blocks.TextBlock(
                                                        required=True
                                                    ),
                                                ),
                                                (
                                                    "author",
                                                    wagtail.core.blocks.RichTextBlock(
                                                        features=["link"], required=True
                                                    ),
                                                ),
                                                (
                                                    "author_image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        ),
                                        min_num=2,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "standalone_cta",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "cta",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "text",
                                                wagtail.core.blocks.CharBlock(
                                                    label="CTA text",
                                                    max_length=255,
                                                    required=False,
                                                ),
                                            ),
                                            (
                                                "cta_page",
                                                wagtail.core.blocks.PageChooserBlock(
                                                    label="CTA page", required=False
                                                ),
                                            ),
                                            (
                                                "cta_url",
                                                wagtail.core.blocks.URLBlock(
                                                    label="CTA URL", required=False
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                                (
                                    "description",
                                    wagtail.core.blocks.TextBlock(
                                        label="Short description",
                                        max_length=100,
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "teaser",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "page",
                                    wagtail.core.blocks.PageChooserBlock(
                                        page_type=["blog.BlogPage"], required=False
                                    ),
                                ),
                                (
                                    "url_chooser",
                                    wagtail.core.blocks.URLBlock(required=False),
                                ),
                                (
                                    "image_for_external_link",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "heading_for_external_link",
                                    wagtail.core.blocks.TextBlock(required=False),
                                ),
                                (
                                    "subheading_for_ext_link",
                                    wagtail.core.blocks.TextBlock(
                                        label="Subheading for external link",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "video",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "autoplay",
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False, required=False
                                    ),
                                ),
                                ("video", wagtailmedia.blocks.VideoChooserBlock()),
                            ]
                        ),
                    ),
                ]
            ),
        ),
    ]
