from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtailseo.models import SeoMixin, SeoType

from prometal.settings.base import FULL_RICHTEXT_FEATURES


class HomePage(SeoMixin, Page):
    template = "prometal/homepage.html"
    max_count = 1

    header_title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        default="Custom and precision sheet metal",
    )
    header_description = models.TextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("header_title"),
                FieldPanel("header_description"),
            ],
            "Landing header section",
            classname="wagtailuiplus__panel--collapsed",
        )
    ]

    seo_content_type = SeoType.WEBSITE

    promote_panels = SeoMixin.seo_meta_panels + SeoMixin.seo_struct_panels

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)

    #     return context
