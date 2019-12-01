class Account:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return "Balance: {:.2f}".format(self.balance)

    def update_balance(self):
        self.balance *= self.year_interest


class DebitAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)
        YEAR_INTEREST = 0.02
        self.year_interest = YEAR_INTEREST + 1

class SavingsAccount(Account):
    def __init__(self, balance):
        INTEREST_RATE = 0.05
        BONUS_RATE = 0.10
        Account.__init__(self, balance)
        self.year_interest = INTEREST_RATE + BONUS_RATE + 1


def print_accounts(accounts):
    for account in accounts:
        print(account)

def update_accounts(accounts):
    for account in acounts:
        account.update_balance()