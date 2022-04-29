"""
Name: off chain
Author: Blas Moyano - Challenge Ripio - Copyright (C) 2022
Functionality: Views
"""

from django.http import Http404
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from balance.models import Ticker, Balance, BalanceEntry
from balance.serializers import (
    TickerSerializer,
    BalanceSerializer,
    OperationSerializer,
    OperationPeerToPeerSerializer,
    BalanceEntrySerializer,
)
from balance.utils.operations import Operation
from .exception import AmountBaseClass

OPERATION = Operation()


class UserValidPermission(permissions.BasePermission):
    """
    verify token
    """

    message = "user path and user token not equal"

    def has_permission(self, request, view):
        request_id_user = request.user.id
        view_id_user = view.kwargs["id"]
        try:
            if int(request_id_user) != int(view_id_user):
                return False
        except TypeError:
            return False
        return True


class ListCreateTicker(ListCreateAPIView):
    """get and post ticker"""

    permission_classes = (IsAdminUser,)
    serializer_class = TickerSerializer
    http_method_names = ["get", "post"]

    def get_queryset(self):
        """ get all ticker"""
        return Ticker.objects.all()

    def post(self, request, *args, **kwargs):
        """ create a new ticker """
        return self.create(request, *args, **kwargs)


class ListBalanceForMe(ListAPIView):
    """get list to balance for user"""

    permission_classes = (UserValidPermission, IsAuthenticated)
    serializer_class = BalanceSerializer
    lookup_url_kwarg = "id"
    queryset = Balance.objects.filter()
    http_method_names = ["get"]

    def get_queryset(self):
        """ get all balance for user """
        id_user = self.kwargs.get(self.lookup_url_kwarg)

        try:
            return Balance.objects.filter(id=id_user)
        except ValueError:
            raise Http404


class ListBalanceEntryForId(ListAPIView):
    serializer_class = BalanceEntrySerializer
    permission_classes = (IsAdminUser,)
    lookup_url_kwarg = "id"
    queryset = BalanceEntry.objects.filter()
    http_method_names = ["get"]

    def get_queryset(self):
        """ get all transaction for user """

        id_user = self.kwargs.get(self.lookup_url_kwarg)

        try:
            return BalanceEntry.objects.filter(user=id_user)
        except ValueError:
            raise Http404


class ListBalanceForId(ListAPIView):
    """get list to balance for user"""

    permission_classes = (IsAdminUser,)
    serializer_class = BalanceSerializer
    lookup_url_kwarg = "id"
    queryset = Balance.objects.filter()
    http_method_names = ["get"]

    def get_queryset(self):
        """ get all balance for user """
        id_user = self.kwargs.get(self.lookup_url_kwarg)
        try:
            return Balance.objects.filter(id=id_user)
        except ValueError:
            raise Http404


class CreateBalance(CreateAPIView):
    """ create a new balance """

    permission_classes = (IsAuthenticated,)
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


class Operations(CreateAPIView):
    """Execute a operation"""

    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = "operation_type"
    serializer_class = OperationSerializer

    def post(self, request, *args, **kwargs):
        operation_type = self.kwargs.get(self.lookup_url_kwarg)
        try:
            ticker_id = int(request.data["ticker_id"])
            amount = float(request.data["amount"])
        except ValueError:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "ticker or amount required integer"},
            )
        try:
            balance_for_user = Balance.objects.select_for_update().get(
                user=request.data["user"], ticker=ticker_id
            )
        except Exception:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "Balance matching query does not exist"},
            )
        if not balance_for_user:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "balancer not exist for user"},
            )
        try:
            message = OPERATION.dispacher_operation(
                operation_type=operation_type, balance=balance_for_user, amount=amount
            )
        except AmountBaseClass:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "The amount is higher than what you have"},
            )
        if OPERATION.SUCCESS == message:
            return Response(
                status=status.HTTP_200_OK,
                data={"message": f"operation {operation_type} success"},
            )
        elif OPERATION.FAIL_AMOUNT == message:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    "message": f"operation {operation_type} Fail."
                    f" The user does not have enough amount"
                },
            )
        else:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": f"operation {operation_type} fail"},
            )


class PeerToPeer(CreateAPIView):
    serializer_class = OperationPeerToPeerSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        if request.data["user_sender_id"] == request.data["user_receiver_id"]:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "users cannot be the same"},
            )
        try:
            ticker_id = int(request.data["ticker_id"])
            amount = float(request.data["amount"])
        except ValueError:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "ticker or amount required integer"},
            )

        try:
            balance_user_sender = Balance.objects.select_for_update().get(
                user=request.data["user_sender_id"], ticker=ticker_id
            )
            balance_user_receiver = Balance.objects.select_for_update().get(
                user=request.data["user_receiver_id"], ticker=ticker_id
            )
        except Exception:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "Balance matching query does not exist"},
            )

        if not balance_user_sender or not balance_user_receiver:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "balancer not exist for user"},
            )

        message = OPERATION.peer_to_peer(
            amount=amount,
            balancer_sender=balance_user_sender,
            balancer_receiver=balance_user_receiver,
        )

        if OPERATION.SUCCESS == message:
            return Response(
                status=status.HTTP_200_OK,
                data={"message": "operation peer to peer success"},
            )
        else:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "operation peer to peer fail"},
            )
