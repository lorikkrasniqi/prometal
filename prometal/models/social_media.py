from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel


@register_setting(icon="user")
class SocialMediaSettings(BaseSiteSetting):
    """Social media links for the website"""

    facebook_page = models.URLField(blank=True, max_length=255)

    twitter_page = models.URLField(blank=True, max_length=255)

    linkedin_page = models.URLField(blank=True, max_length=255)

    instagram_page = models.URLField(blank=True, max_length=255)

    youtube_page = models.URLField(blank=True, max_length=255)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("facebook_page"),
                FieldPanel("twitter_page"),
                FieldPanel("linkedin_page"),
                FieldPanel("instagram_page"),
                FieldPanel("youtube_page"),
            ],
            heading=_("ProMetal Social Media Accounts"),
        ),
    ]

    class Meta:
        verbose_name = _("Social Media Links")
