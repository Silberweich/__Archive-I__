class Category:
    # Attribute
    # ledger = list()
    # _category = str()
    # balance = float()
    # Constructor
    def __init__(self, _category: str):
        self.ledger = list()
        self.balance = 0.00
        self._category = _category

        self.surplus = 0.00 #just in case
        self.minus = 0.00   #just in case

    # Meth
    def deposit(self, amount:float, description:str = ""):
        self.ledger.append({"amount" : amount, "description": description})
        self.balance += amount
        self.surplus += amount
    
    def withdraw(self, amount:float, description:str = "") -> bool:
        neg_amount = 0 - amount
        if self.check_funds(amount):
            self.ledger.append({"amount" : neg_amount, "description": description})
            self.balance += neg_amount
            self.minus -= neg_amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        return self.balance

    def get_surplus(self) -> float:
        return self.surplus

    def get_minus(self) -> float:
        return self.minus

    def transfer(self, amount:float, transfer_to) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {transfer_to._category}")
            transfer_to.deposit(amount, f"Transfer from {self._category}")
            return True
        else:
            return False

    def check_funds(self, amount:float):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self) -> str:
        title = f"{self._category:*^30}\n"
        items = str()
        total = float()

        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23}" + \
            f"{self.ledger[i]['amount']:>7.2f}" + '\n'

            total += self.ledger[i]['amount']

        output = title + items + "Total: " + str(total)
        return output

def create_spend_chart(categories):
    total_spent = 0
    all_percent = []
    names = []

    # Assign name to list for print
    for category in categories:
        names.append(category._category)

    # This will give total spent
    for instance in categories:
        total_spent += instance.get_minus()
    
    # This will give percentage of each
    for instance in categories:
        all_percent.append(int((instance.get_minus() / total_spent) * 100))

    #######################################################################

    # Start of the graph
    return_string = "Percentage spent by category\n"

    # This print top part of the graph
    for i in range (100, -1, -10):
        graph_dot = " "
        for percent in all_percent:
            if percent >= i:
                graph_dot += "o  "
            else:
                graph_dot += "   "

        return_string += str(i).rjust(3) + "|" + graph_dot + ("\n")
    
    # The bottom line separategraph and text
    bottom_line = "-" + "---" * len(categories)

    by_line = ""
    longest_name = max(names, key=len)

    for x in range(len(longest_name)):
        #each line start with emptiness
        name_by_line = '     '

        for name in names:
            if x >= len(name):
                name_by_line += "   "
            else:
                name_by_line += name[x] + "  "

        # Last line = no new line
        if x < len(longest_name) - 1:
            name_by_line += '\n'

        by_line += name_by_line

    return_string += bottom_line.rjust(len(bottom_line)+4) + "\n" + by_line

    print(return_string)
    return return_string

# NNN|-^--^--^--
# -NN|-^--^--^--
# -NN|-^--^--^--
# -NN|-^--^--^--
# -NN|-^--^--^--
# -NN|-^--^--^--
# -NN|-^--^--^--
# -NN|-^--^--^--
# -NN|-^--^--^--
# --N|-^--^--^--
# ----==========
# -----A--A--A--
# -----A--A--A--
# -----A--A--A--
# -----A--A--A--
# -----A--A--A--
# -----A--A--A--