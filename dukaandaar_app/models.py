from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dukaan(models.Model):
    # dukaan_id is dukaan_user_id in django
    dukaan_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    dukaan_name = models.CharField(max_length=250, blank=True, null=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    active_status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        if self.dukaan_name:
            return self.dukaan_name
        return str(self.id)

class Tag(models.Model):
    tag = models.CharField(max_length=250, blank=True, null=True)
    class Meta:
        ordering = ['tag']
    def __str__(self):
        return self.tag

class Mal(models.Model):
    name = models.CharField(max_length=250, null=True, unique=True)
    description = models.CharField(max_length=250, blank=True, null=True, unique=True)
    dukaan = models.ForeignKey(
        Dukaan,
        related_name="mal_dukaan",
        on_delete=models.CASCADE,
    )
    quantity = models.CharField(max_length=20, blank=True, null=True, default="1")
    photo_link = models.CharField(max_length=200, blank=True, null=True)
    selling_price = models.CharField(max_length=20, blank=True, null=True)
    tags = models.ManyToManyField(
        Tag,
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

    def __str__(self):
        return self.name

