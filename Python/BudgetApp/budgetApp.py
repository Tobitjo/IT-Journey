class Category:
    def __init__(self, name):
        self.name = name 
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    
    def get_balance(self):
        balance = 0
        for element in self.ledger:
            balance += element['amount']
        return balance


    def transfer(self, amount, Category):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {Category.name}')
            Category.deposit(amount,f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
    
    def __str__(self):
        title = self.name.center(30,'*')
        result = title + '\n'

        for element in self.ledger:
            description = element['description'][:23].ljust(23)
            amount = f"{element['amount']:>7.2f}"
            result += f"{description}{amount}\n"

        result += f"Total: {self.get_balance():.2f}"
        return result

    def create_spend_chart(categories):
        total_spent = 0
        spent_per_category = []
        
        for category in categories:
            spent = sum(-entry['amount'] for entry in category.ledger if entry['amount'] < 0)
            spent_per_category.append(spent)
            total_spent += spent
        
        percentages = [int((spent / total_spent) * 100) // 10 * 10 for spent in spent_per_category]
        
        chart = "Percentage spent by category\n"
        for i in range(100, -1, -10):
            chart += str(i).rjust(3) + "|"
            for percentage in percentages:
                chart += " o " if percentage >= i else "   "
            chart += " \n"
        
        chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
        
        max_length = max(len(category.name) for category in categories)
        for i in range(max_length):
            chart += "     "
            for category in categories:
                chart += f" {category.name[i] if i < len(category.name) else ' '} "
            chart += " \n"
        
        return chart.strip()

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(clothing)
print(Category.create_spend_chart([food, clothing]))