"""
Name: off chain
Author: Blas Moyano - Challenge Ripio - Copyright (C) 2022
Functionality: Views
"""

# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView

# from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from balance.models import Ticker, Balance
from balance.serializers import TickerSerializer, BalanceSerializer
from .operations import Operation


OPERATION = Operation()


class UserValidPermission(permissions.BasePermission):
    """
    verify token
    """

    message = "user path and user token not equal"

    def has_permission(self, request, view):
        request_id_user = request.user.id
        view_id_user = view.kwargs["id"]
        if int(request_id_user) != int(view_id_user):
            return False
        return True


class ListCreateTicker(ListCreateAPIView):
    """get and post ticker"""

    # permission_classes = (IsAdminUser,)
    serializer_class = TickerSerializer
    http_method_names = ["get", "post"]

    def get_queryset(self):
        """ get all ticker"""
        return Ticker.objects.all()

    def post(self, request, *args, **kwargs):
        """ create a new ticker """
        return self.create(request, *args, **kwargs)


class ListBalanceForId(ListAPIView):
    """get list to balance for user"""

    # permission_classes = (UserValidPermission, IsAdminUser)
    serializer_class = BalanceSerializer
    lookup_url_kwarg = "id"
    queryset = Balance.objects.filter()
    http_method_names = ["get"]

    def get_queryset(self):
        """ get all balance for user """
        id_user = self.kwargs.get(self.lookup_url_kwarg)
        return Balance.objects.filter(id=id_user)


class CreateBalance(CreateAPIView):
    """ create a new balance """

    # permission_classes = (IsAuthenticated,)
    serializer_class = BalanceSerializer

    def post(self, request, *args, **kwargs):
        balance_for_user = Balance.objects.filter(
            user=request.user.id, ticker=request.data["ticker_id"]
        )

        if balance_for_user:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "the balance with user and ticker exists"},
            )

        return self.create(request, *args, **kwargs)


class Airdrop(CreateAPIView):
    """Create a airdrop"""

    # permission_classes = (IsAuthenticated,)
    serializer_class = BalanceSerializer

    def post(self, request, *args, **kwargs):
        balance_for_user = Balance.objects.filter(
            user=1, ticker=request.data["ticker_id"]
        )

        if not balance_for_user:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "balancer not exist for user"},
            )
        elif len(balance_for_user) > 1:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "the user has more than balancer"},
            )

        message = OPERATION.airdrop(
            account=request.data["account"], balance_user=balance_for_user[0]
        )

        if OPERATION.SUCCESS == message:
            return Response(
                status=status.HTTP_200_OK, data={"message": "airdrop success"}
            )
        else:
            return Response(
                status=status.HTTP_404_NOT_FOUND, data={"message": "airdrop fail"}
            )
