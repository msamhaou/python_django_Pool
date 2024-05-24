class hotBeverage:
    def __init__(self, price=0.30, name="hot beverage"):
        self.price = price;
        self.name = name;
        pass;
    def description(self):
        return "Just some hot water in a cup.";
    def __str__(self):
        return(f"name: {self.name}\nprice: {self.price}\ndecription: {self.description()}");

class Coffee(hotBeverage):
    def __init__(self, price=0.40, name="coffee"):
        hotBeverage.__init__(self, name, price);
        pass;
    def description(self):
        return "A coffee, to stay awake."

class Tea(hotBeverage):
    def __init__(self, price=0.30, name="tea"):
        super().__init__(price, name);

class Choclate(hotBeverage):
    def __init__(self, price=0.50, name="chocolate"):
        super().__init__(price, name)
    def description(self):
        return "Chocolate, sweet chocolate..."
    
class Cappuccino(hotBeverage):
    def __init__(self,price=0.45, name="cappuccino"):
        super().__init__(price, name);
    def description(self):
        return "Un po’ di Italia nella sua tazza!"
