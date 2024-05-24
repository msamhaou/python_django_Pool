import beverages;
from machine import CoffeeMachine ;

machine = CoffeeMachine();
for i in range(12):
    try:
        print(machine.serve(beverages.Tea()))
        print(i)
    except Exception as e:
        print(e);
machine.repair();
for i in range(12):
    try:
        print(machine.serve(beverages.Choclate()))
        print(i)
    except Exception as e:
        print(e);