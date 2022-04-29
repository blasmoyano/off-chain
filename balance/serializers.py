"""
Name: off chain
Author: Blas Moyano - Challenge Ripio - Copyright (C) 2022
Functionality: serializers
"""

from rest_framework import serializers
from .models import Ticker, Balance, BalanceEntry
from authentication.models import CustomUser


class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = "__all__"


class BalanceSerializer(serializers.ModelSerializer):
    ticker = TickerSerializer(read_only=True)
    ticker_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Ticker.objects.all(), source="ticker"
    )

    class Meta:
        model = Balance
        fields = ("id", "create_date", "update_date", "amount", "ticker", "ticker_id")

    def create(self, validated_data):
        request = self.context.get("request", None)
        if request:
            user_id = request.user.id
        if user_id:
            validated_data["user"] = CustomUser.objects.filter(id=user_id).first()
        return Balance.objects.create(**validated_data)


class OperationSerializer(serializers.ModelSerializer):
    ticker = TickerSerializer(read_only=True)
    ticker_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Ticker.objects.all(), source="ticker"
    )

    class Meta:
        model = Balance
        fields = (
            "id",
            "create_date",
            "update_date",
            "amount",
            "ticker",
            "ticker_id",
            "user",
        )


class OperationPeerToPeerSerializer(serializers.ModelSerializer):
    ticker = TickerSerializer(read_only=True)
    ticker_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Ticker.objects.all(), source="ticker"
    )

    user_sender = CustomUserSerializer(read_only=True)
    user_sender_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=CustomUser.objects.all(),
        source="User_sender",
        label="user sender",
    )
    user_receiver = CustomUserSerializer(read_only=True)
    user_receiver_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=CustomUser.objects.all(),
        source="User_receiver",
        label="user receiver",
    )

    class Meta:
        model = Balance
        fields = (
            "id",
            "create_date",
            "update_date",
            "amount",
            "ticker",
            "ticker_id",
            "user_receiver",
            "user_receiver_id",
            "user_sender",
            "user_sender_id",
        )


class BalanceEntrySerializer(serializers.ModelSerializer):
    balance = BalanceSerializer(read_only=True)
    balance_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Balance.objects.all(), source="balance"
    )

    class Meta:
        model = BalanceEntry
        fields = "__all__"
