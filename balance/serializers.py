"""
Name: off chain
Author: Blas Moyano - Challenge Ripio - Copyright (C) 2022
Functionality: serializers
"""

from rest_framework import serializers
from authentication.models import CustomUser
from .models import Ticker, Balance


class TickerSerializer(serializers.ModelSerializer):
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
        fields = ("id", "create_date", "update_date", "account", "ticker", "ticker_id")

    def create(self, validated_data):
        request = self.context.get("request", None)
        if request:
            user_id = request.user.id
        if user_id:
            validated_data["user"] = CustomUser.objects.filter(id=user_id).first()
        return Balance.objects.create(**validated_data)
