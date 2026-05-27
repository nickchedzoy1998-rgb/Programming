# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'
    
class SuperGroup:
    def __init__(self, name: str, location: str):
        self.__name = name
        self.__location = location
        self.__members = []

    @property
    def name(self):
        return self.__name
    
    @property
    def location(self):
        return self.__location
    
    @name.setter
    def name(self, name:str):
        self.__name = name

    @location.setter
    def location(self, location:str):
        self.__location = location

    def add_member(self, hero: SuperHero):
        self.__members.append(hero)

    def print_group(self):
        print(self.name, self.location)
        print('Members:')
        for member in self.__members:
            print(member.__str__())


if __name__ == '__main__':
    superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
    invisible = SuperHero("Invisible Inca", "Invisibility")
    revengers = SuperGroup("Revengers", "Emerald City")

    revengers.add_member(superperson)
    revengers.add_member(invisible)
    revengers.print_group()