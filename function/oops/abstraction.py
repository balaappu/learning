from abc import ABC,abstractmethod
#parent class named employee
class employee(ABC):
    def __init__(self):
        self.perform="performance"

    @ abstractmethod
    def performance(self):
        print("working hour")

class production(employee):
    def __init__(self):
        super().__init__()

    def performance(self):
        print(self.perform)
        print("production based on performance")

vimal=production()
vimal.performance()        
    