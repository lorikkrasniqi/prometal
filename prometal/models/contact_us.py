from django.db import models
from wagtail.core.models import Page
from wagtailseo.models import SeoMixin, SeoType
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel


class ContactUsPage(SeoMixin, Page):
    template = "prometal/contact_us.html"

    max_count = 1

    parent_page_types = ["prometal.HomePage"]

    contact_form_title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="Get in touch",
    )

    contact_form_description = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="Our friendly team would love to hear from you.",
    )

    submit_button_text = models.CharField(
        max_length=255, null=False, blank=False, default="Send message"
    )

    company_location_latitude = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="42.302032967279764",
    )

    company_location_longitude = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="21.207894876779495",
    )

    company_pin_text = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="ProMetal SH.P.K.",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("contact_form_title"),
                FieldPanel("contact_form_description"),
                FieldPanel("submit_button_text"),
            ],
            "Contact form",
            classname="wagtailuiplus__panel--collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel("company_location_latitude"),
                FieldPanel("company_location_longitude"),
                FieldPanel("company_pin_text"),
            ],
            "Company map",
            classname="wagtailuiplus__panel--collapsed",
        ),
    ]

    seo_content_type = SeoType.WEBSITE

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        from ..forms import ContactForm

        contact_form = ContactForm()

        context["contact_form"] = contact_form

        return context
