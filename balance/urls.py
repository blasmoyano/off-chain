"""
Name: off chain
Author: Blas Moyano - Challenge Ripio - Copyright (C) 2022
Functionality: Urls
"""

from django.urls import path, re_path
from balance import views

urlpatterns = [
    path("ticker/", views.ListCreateTicker.as_view(), name="ticker"),
    path(
        "balance/me/<id>/",
        views.ListBalanceForMe.as_view(),
        name="get_by_id_balance_for_me",
    ),
    path(
        "balance/user/<id>/", views.ListBalanceForId.as_view(), name="get_by_id_balance"
    ),
    path(
        "transaction/user/<id>/",
        views.ListBalanceEntryForId.as_view(),
        name="get_transaction",
    ),
    path("balance/create/", views.CreateBalance.as_view(), name="create_balance"),
    re_path(
        r"operation/(?P<operation_type>\bairdrop\b|\bburn\b)/",
        views.Operations.as_view(),
        name="create_operation",
    ),
    path(
        "operation/peer_to_peer/",
        views.PeerToPeer.as_view(),
        name="create_peer_to_peer",
    ),
]
