"""
Name: off chain
Author: Blas Moyano - Challenge Ripio - Copyright (C) 2022
Functionality: Urls
"""

from django.urls import path
from balance import views

urlpatterns = [
    path("ticker/", views.ListCreateTicker.as_view(), name="ticker"),
    path("me/<id>/", views.ListBalanceForId.as_view(), name="get_by_id_balance"),
    path("create/", views.CreateBalance.as_view(), name="create_balance"),
    path("airdrop/", views.Airdrop.as_view(), name="create_airdrop"),
]
