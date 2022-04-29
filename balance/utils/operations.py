"""
Name: off chain
Author: Blas Moyano - Challenge Ripio - Copyright (C) 2022
Functionality: operations
"""

from balance.models import BalanceEntry
from balance.exception import AmountBaseClass
from .cryptographys import CustomCryptography


class Operation:
    SUCCESS = "success"
    FAIL = "fail"
    FAIL_AMOUNT = "amount_fail"

    @staticmethod
    def create_balance_entry(balance, amounts, operation_type):
        try:
            BalanceEntry(
                balance=balance,
                user_id=balance.user.id,
                amount=amounts["received"],
                amount_before=amounts["before"],
                amount_after=amounts["after"],
                operation_type=operation_type,
            ).save()
        except Exception:
            return Operation.FAIL

        return Operation.SUCCESS

    @staticmethod
    def rollback(balance, amounts, hash_old):
        balance.amount = amounts["before"]
        balance.hash = hash_old
        balance.save()

    def dispacher_operation(self, operation_type, balance, amount):
        if operation_type == "burn":
            amounts, balance, hash_old = self.burn(amount=amount, balance_user=balance)
        elif operation_type == "airdrop":
            amounts, balance, hash_old = self.airdrop(
                amount=amount, balance_user=balance
            )
        else:
            return self.FAIL

        message = self.create_balance_entry(
            balance=balance, amounts=amounts, operation_type=operation_type
        )
        if message == Operation.FAIL:
            self.rollback(balance, amounts, hash_old)

        return message

    def airdrop(self, amount, balance_user):

        amounts = {
            "before": balance_user.amount,
            "after": balance_user.amount + float(amount),
            "received": amount,
        }
        balance_user.amount = amounts["after"]
        data = (
            f"amount: {balance_user.amount}. user: {balance_user.user}. "
            f"ticker: {balance_user.ticker}. date: {balance_user.update_date}"
        )
        balance_user.hash = CustomCryptography().encrypt(bytes(data))
        hash_old = balance_user.hash
        balance_user.save()
        return amounts, balance_user, hash_old

    def burn(self, amount, balance_user):

        if float(amount) > balance_user.amount:
            raise AmountBaseClass("the amount is higher than what you have")

        amounts = {
            "before": balance_user.amount,
            "after": balance_user.amount - float(amount),
            "received": amount,
        }
        balance_user.amount = amounts["after"]
        data = (
            f"amount: {balance_user.amount}. user: {balance_user.user}. "
            f"ticker: {balance_user.ticker}. date: {balance_user.update_date}"
        )
        hash_old = balance_user.hash
        balance_user.hash = CustomCryptography().encrypt(str.encode(data))
        balance_user.save()

        return amounts, balance_user, hash_old

    def peer_to_peer(self, amount, balancer_sender, balancer_receiver):
        amounts_sender, balance_sender = self.burn(amount, balancer_sender)

        message_sender = self.create_balance_entry(
            balance=balance_sender,
            amounts=amounts_sender,
            operation_type="peer_to_peer",
        )

        if message_sender == Operation.FAIL:
            self.rollback(balance_sender, amounts_sender)

        amounts_receiver, balancer_receiver = self.airdrop(amount, balancer_receiver)

        message_receiver = self.create_balance_entry(
            balance=balancer_receiver,
            amounts=amounts_receiver,
            operation_type="peer_to_peer",
        )

        if message_receiver == Operation.FAIL:
            self.rollback(amounts_receiver, balancer_receiver)

        return self.SUCCESS
