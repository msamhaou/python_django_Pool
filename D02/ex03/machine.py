import random;
import beverages;
from beverages import hotBeverage;

class CoffeeMachine:
    def __init__(self):
        self.obsolescence = 10;
        self.broken = 0;
        pass;
    def repair(self):
        self.obsolescence = 10;
        self.broken = 0;
        pass
    
    class EmptyCup(hotBeverage):
        def __init__(self,price=0.90,name="Empty Cup"):
            super().__init__(price, name);
        def description(self):
            return "An empty cup?! Gimme my money back!";
        pass
    
    def serve(self,beverage):
        if (self.obsolescence == 0):
            raise self.BrokenMachineException();
        self.obsolescence -= 1;
        bev = [self.EmptyCup(), beverage];
        return(bev[random.randrange(2)]);

    class BrokenMachineException(Exception):
        def __init__(self, msg="This coffee machine has to be repaired."):
            super().__init__(msg)
        pass


