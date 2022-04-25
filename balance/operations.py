"""
Name: off chain
Author: Blas Moyano - Challenge Ripio - Copyright (C) 2022
Functionality: operations
"""

from .models import BalanceEntry


class Operation:
    SUCCESS = "success"
    FAIL = "fail"

    def airdrop(self, account, balance_user):
        account_before = balance_user.account
        account_after = balance_user.account + float(account)

        balance_user.account = account_after
        balance_user.save()

        BalanceEntry(
            balance=balance_user,
            account=account,
            account_before=account_before,
            account_after=account_after,
            operation_type="airdrop",
        ).save()
        return self.SUCCESS
