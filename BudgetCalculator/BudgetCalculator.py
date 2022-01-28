

class Category:


    # Override self
    def __init__(self, Category):
        self.category = Category
        self.ledger = []
        self.total = 0
        self.spending_log = []
        self.total_spending = 0

    # Override when object is called to a string function
    def __str__(self):


        lines = []

        # Header 30 total chars long
        lines.append(self.category.center(30, "*") + "\n")

        # Iterate through ledger transactions
        for transaction in self.ledger:

            # Format transaction amounts
            amount_formatted = format(transaction['amount'], '.2f')

            # Format description
            if len(transaction['description']) >= len(lines[0]) - len(amount_formatted):
                description_formatted = transaction['description'][:len(lines[0]) - len(amount_formatted) - 2]
            else:
                description_formatted = transaction['description']

            # Append description and amount to lines[]
            lines.append(description_formatted + (" " * (len(lines[0]) - len(amount_formatted) - len(description_formatted) - 1)) + amount_formatted + "\n")

        # Append total to lines []
        lines.append(f"Total: {self.total}")

        return "".join(lines)




    def update_balance(self):
        accumulator = 0
        for each in self.ledger:
            if each['amount'] < 0:

                # Negative transactions to list of positives
                self.spending_log.append(each['amount'] * -1)

                # Accumulate total spending
                self.total_spending = sum(self.spending_log)
            accumulator += each['amount']

        # Transaction total
        self.total = accumulator





    def deposit(self, amount, description=""):

        # Record transaction
        self.ledger.append({"amount": amount, "description": description})

        # Update total
        self.update_balance()





    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": amount * -1, "description": description})
            self.update_balance()
            return self.check_funds(amount)

        return self.check_funds(amount)



    def get_balance(self):
        return float("%.2f" % round(self.total, 2))




    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.total += amount
            self.ledger.append({"amount": amount * -1, "description": f"Transfer to {category.category}"})
            category.ledger.append({"amount": amount, "description": f"Transfer from {self.category}"})
            self.update_balance()
            category.update_balance()
            return self.check_funds(amount)
        else:
            return self.check_funds(amount)




    def check_funds(self, amount):
        return self.total >= amount







def create_spend_chart(categories):

    lines = []

    lines.append("Percentage spent by category\n")
    x_labels = [category.category for category in categories]

    total_spending = 0
    for category in categories:
        for each in category.ledger:
            if each['amount'] < 0:
                total_spending += each['amount'] * -1

    x_values = []
    for category in categories:

        x_values.append(round(category.total_spending / total_spending * 100) - round(((category.total_spending / total_spending * 100) % 10)))



    longest_category = len(max(x_labels, key=len))



    for y in range(100, -10, -10):

        if len(str(y)) < 3:
            lines.append(" " * (3 - len(str(y))) + str(y) + "| ")

            for value in x_values:
                if value >= y:
                    lines.append("o  ")
                else:
                    lines.append(" " * 3)


        else:
            lines.append(str(y) + "| ")

            for value in x_values:
                if value >= y:
                    lines.append("o  ")
                else:
                    lines.append(" " * 3)

        lines.append("\n")




    lines.append((" " * 4) + ("-" * (len("".join(lines[1:4])) - 1)) + "\n")




    for index in range(longest_category):
        lines.append(" " * 5)

        for each in x_labels:

            try:
                lines.append(list(each)[index] + "  ")
            except:
                lines.append("   ")


        lines.append("\n")



    return print("".join(lines[:-1]))

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)



create_spend_chart([business, food, entertainment])

