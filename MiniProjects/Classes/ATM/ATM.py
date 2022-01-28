class Account:
    def __init__(self,ID):
        self.id = ID


class Chequeing_Account(Account):

    def __init__(self, name, ODprotection, ID, initial_deposit)
        Account.__init__(self, ID)

        self.name = name
        self.ODprotection = ODprotection
        self.amount = initial_deposit

    def deposit(self, deposit):
        self.amount += deposit
        return f"{deposit} deposited to {__class__.__name__}\nTotal: {self.amount}"

    # withdraw from account
    def withdraw(self, withdraw):
        if self.amount < withdraw:
            return f"Cannot withdraw more than {self.amount}"
        if withdraw < 0.01:
            return f"{withdraw} is not a valid positive number. Please enter a positive number"

        self.amount -= withdraw
        return f"{withdraw} withdrew from {__class__.__name__}"

    def total(self):
        return f"Total: {self.amount}"
