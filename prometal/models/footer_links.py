from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.core.models import Orderable
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


class FooterLinks(Orderable):
    page = ParentalKey("FooterColumns", related_name="footer_links")

    text = models.CharField(max_length=100, null=True)
    link = models.URLField(max_length=255)
    new_tab = models.BooleanField(default=False)

    panels = [
        FieldPanel("text"),
        FieldPanel("link"),
        FieldPanel("new_tab"),
    ]


class FooterColumns(ClusterableModel, Orderable):
    page = ParentalKey("FooterLinksSettings", related_name="footer_columns")

    column_title = models.CharField(blank=True, max_length=100)

    panels = [
        FieldPanel("column_title"),
        InlinePanel(
            "footer_links",
            label="Footer links",
            max_num=4,
            heading="Add a footer link",
            help_text="You can add 4 footer links maximum per column",
        ),
    ]


@register_setting(icon="link")
class FooterLinksSettings(BaseSiteSetting, ClusterableModel):

    panels = [
        InlinePanel(
            "footer_columns",
            label="Footer columns",
            max_num=3,
            heading="Add a footer column",
            help_text="You can add 3 footer columns maximum",
        ),
    ]

    class Meta:
        db_table = "footer_links"
        verbose_name = _("Footer Link")
        verbose_name_plural = _("Footer Links")
