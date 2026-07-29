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
        return f'{title}'


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)