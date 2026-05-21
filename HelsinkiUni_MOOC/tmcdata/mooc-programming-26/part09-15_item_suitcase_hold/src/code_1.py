# Write your solution here:

class Item:
    def __init__(self, name: str, weight: float):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f'{self.__name} ({self.__weight} kg)'
    
    @property
    def name(self):
        return self.__name
    
    @property
    def weight(self):
        return self.__weight

    
class Suitcase:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []

    def add_item(self, item:Item):
        if (self.max_weight - self.combined_weight() - item.weight) >= 0:
            self.items.append(item)

    def __str__(self):
        item_weights = self.combined_weight()
        if len(self.items) == 1:
            item_string = 'item'
        else:
            item_string = 'items'

        return f'{len(self.items)} {item_string} ({item_weights} kg)'
    
    def print_items(self):
        for item in self.items:
            return item.__str___()
        
    def combined_weight(self):
        return sum(item.weight for item in self.items)
    
    def heaviest_item(self):
        i = None
        heaviest_weight = 0

        for item in self.items:
            if item.weight > heaviest_weight:
                i = item
                heaviest_weight = item.weight()

        return i.__str__()
    

class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.cases = []

    def add_suitcase(self, suitcase:Suitcase):
        if (self.max_weight - suitcase.combined_weight() - sum(s.combined_weight() for s in self.cases)) >= 0:
            self.cases.append(suitcase)

    def __str__(self):
        y = self.max_weight - (sum(sc.combined_weight() for sc in self.cases))
        return f'{len(self.cases)} suitcases, space for {y} kg'
    
    def print_items(self):
        for case in self.cases:
            for item in case.items:
                print(item.__str__())

if __name__ == '__main__':

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()