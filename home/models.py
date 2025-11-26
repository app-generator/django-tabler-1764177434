# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    notes = models.TextField(max_length=255, null=True, blank=True)
    target_price = models.IntegerField(null=True, blank=True)
    stop_loss = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Category(models.Model):

    #__Category_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Asset(models.Model):

    #__Asset_FIELDS__
    symbol = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    current_price_source = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField()

    #__Asset_FIELDS__END

    class Meta:
        verbose_name        = _("Asset")
        verbose_name_plural = _("Asset")


class Portfolio(models.Model):

    #__Portfolio_FIELDS__
    owner_user = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Portfolio_FIELDS__END

    class Meta:
        verbose_name        = _("Portfolio")
        verbose_name_plural = _("Portfolio")


class Holding(models.Model):

    #__Holding_FIELDS__
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    purchase_price = models.IntegerField(null=True, blank=True)
    purchased_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Holding_FIELDS__END

    class Meta:
        verbose_name        = _("Holding")
        verbose_name_plural = _("Holding")



#__MODELS__END
