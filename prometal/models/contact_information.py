from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel


@register_setting(icon="user")
class ContactInformationSettings(BaseSiteSetting):
    """Contact information for the company"""

    website_url = models.URLField(blank=True, max_length=255)

    email = models.EmailField(blank=True, max_length=100)

    phone_no = models.CharField(blank=True, max_length=100)

    address = models.CharField(blank=True, max_length=255)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("website_url"),
                FieldPanel("email"),
                FieldPanel("phone_no"),
                FieldPanel("address"),
            ],
            heading=_("ProMetal Contact Information"),
        ),
    ]

    class Meta:
        verbose_name = _("Contact Information")
