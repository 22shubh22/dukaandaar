from django.db import models

# Create your models here.

class Mal(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True, unique=True)
    description = models.CharField(max_length=250, blank=True, null=True, unique=True)
    dukaan = models.OneToOneField(
        Dukaan,
        on_delete=models.CASCADE,
        related_name="mal_dukaan",
        null=True,
        blank=True,
        db_column="dukaan",
    )
    quantity = models.CharField(max_length=20, blank=True, null=True)
    photo_link = models.CharField(max_length=200, blank=True, null=True)
    selling_price = models.CharField(max_length=20, blank=True, null=True)
    active_status = models.BooleanField(default=1)
    tags = models.ForeignKey(
        Tags,
        on_delete=models.DO_NOTHING,
        related_name="mal_tag",
        null=True,
        blank=True,
        db_column="tag",
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


    class Meta:
        verbose_name = "Mal"
        verbose_name_plural = "mals" 


class Dukaan(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    mals = models.OneToManyField(
        Mal,
        related_name="mal_dukaan"
        db_column="mal"
    )

class Tag(models.Model):
    tag = models.CharField(max_length=250, blank=True, null=True)
    mals = models.OneToManyField(
        Mal,
        related_name="tag_mal"
        db_column="mal"
    )