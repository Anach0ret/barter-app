from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _



class Ad(models.Model):
    class Condition(models.TextChoices):
        NEW = "new", _("New")
        USED = "used", _("Used")

    class Category(models.TextChoices):
        TECH = "tech", _("Tech")
        CLOTHES = "clothes", _("Clothes")
        DISHES = "Dishes", _("Dishes")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name=_("User"),
    )
    title = models.CharField(_("Title"), max_length=200)
    slug = models.SlugField(_("Slug"), max_length=120, unique=True)
    description = models.TextField(_("Description"))
    image_url = models.URLField(_("Image URL"), blank=True, null=True)
    category = models.CharField(
        _("Category"),
        choices=Category.choices,
        default=Category.TECH,
    )
    condition = models.CharField(
        _("Condition"),
        max_length=10,
        choices=Condition.choices,
        default=Condition.USED,
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Ad")
        verbose_name_plural = _("Ads")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} — {self.user}"

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slug = slugify(self.title)
            while Ad.objects.filter(slug=unique_slug).exists():
                unique_slug = slugify(f'{self.title}-{get_random_string(length=4)}')
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("ad_detail", kwargs={"slug": self.slug})


class BarterRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", _("Pending")
        ACCEPTED = "accepted", _("Accepted")
        DECLINED = "declined", _("Declined")

    ad_sender = models.ForeignKey("Ad", on_delete=models.CASCADE, related_name="sent_barter_requests")
    ad_receiver = models.ForeignKey("Ad", on_delete=models.CASCADE, related_name="received_barter_requests")

    comment = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("ad_sender", "ad_receiver")

    def __str__(self):
        return f"{self.ad_sender} → {self.ad_receiver} [{self.status}]"