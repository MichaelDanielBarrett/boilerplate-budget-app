class Category:

    def __init__(self, name):
        self.ledger = list()
        self.name = name
        self.spend = 0.0

    def deposit(self, amt, desc = ''):
        new_entry = {"amount": amt, "description": desc}
        self.ledger.append(new_entry.copy())

    def withdraw(self, amt, desc = ''):
        new_entry = {"amount": (-1) * amt, "description": desc}
        if self.check_funds(amt):
            self.ledger.append(new_entry.copy())
            return True
        else:
            return False

    def get_balance(self):
        tot = 0
        for item in self.ledger:
            tot += item["amount"]
        return tot

    def transfer(self, amt, dest):
        if self.check_funds(amt):
            self.withdraw(amt, f"Transfer to {dest.name}")
            dest.deposit(amt, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amt):
        if self.get_balance() >= amt:
            return True
        else:
            return False

    def __repr__(self):
        title = f'{self.name:*^30s}\n'
        items = ''
        for item in self.ledger:
            items += f'{item["description"]:<23.23s}{item["amount"]:>7.2f}\n'
        total = f'Total: {self.get_balance():.2f}'
        return title + items + total

    def total_spend(self):
        tot = 0
        for item in self.ledger:
            if item["amount"] < 0:
                tot -= item["amount"]
        return tot
    

def create_spend_chart(categories):
    tot = 0
    for cat in categories:
        cat.spend = cat.total_spend()
        tot += cat.total_spend()
    for cat in categories:
        cat.spend = (cat.spend * 10) // tot
    width = 3 * len(categories)
    txt = 'Percentage spent by category'
    for i in range(0, 11):
        j = 10 - i
        txt += f'\n{j*10:>3d}| '
        for cat in categories:
            if cat.spend >= j:
                txt += 'o  '
            else:
                txt += '   '
    txt += f"\n    -{'-'*width}"
    depth = 0
    for cat in categories:
        if depth < len(cat.name):
            depth = len(cat.name)
    for i in range(0, depth):
        txt += '\n     '
        for cat in categories:
            if i < len(cat.name):
                txt += f'{cat.name[i]}  '
            else:
                txt += '   '
    return txt

