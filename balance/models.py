"""
Name: off chain
Author: Blas Moyano - Challenge Ripio - Copyright (C) 2022
Functionality: Models
"""

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Ticker(models.Model):
    """ Ticker Model """

    ENABLE_CHOICES = ((True, "Enable"), (False, "Disable"))

    name = models.CharField(verbose_name="ticker name", max_length=20)
    code = models.CharField(verbose_name="ticker code", max_length=3, unique=True)
    enable = models.BooleanField(
        choices=ENABLE_CHOICES, verbose_name="Enable", default=True
    )

    class Meta:
        verbose_name = "Ticker"
        verbose_name_plural = "Tickers"
        ordering = ["-code"]

    def __str__(self):
        return self.code


class Balance(models.Model):
    """ Balance Model """

    create_date = models.DateTimeField(auto_now_add=True, verbose_name="creation date")
    update_date = models.DateTimeField(auto_now=True, verbose_name="update date")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user ID")
    ticker = models.ForeignKey(
        Ticker, on_delete=models.CASCADE, verbose_name="ticker ID"
    )
    amount = models.FloatField(verbose_name="amount")
    hash = models.TextField(verbose_name="hash")

    def __str__(self):
        return f"{self.user.username}_{self.ticker}"


class BalanceEntry(models.Model):
    AIRDROP = "airdrop"
    BURN = "burn"
    PEER_TO_PEER = "peer_to_peer"
    OPERATION_CHOICES = [
        (AIRDROP, "Airdrop"),
        (BURN, "Burn"),
        (PEER_TO_PEER, "Peer to Peer"),
    ]

    balance = models.ForeignKey(
        Balance, on_delete=models.CASCADE, verbose_name="balance ID"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user ID")
    amount = models.FloatField(verbose_name="amount received")
    amount_before = models.FloatField(verbose_name="amount before")
    amount_after = models.FloatField(verbose_name="amount after")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="creation date")
    operation_type = models.CharField(
        max_length=12, choices=OPERATION_CHOICES, default=AIRDROP
    )
