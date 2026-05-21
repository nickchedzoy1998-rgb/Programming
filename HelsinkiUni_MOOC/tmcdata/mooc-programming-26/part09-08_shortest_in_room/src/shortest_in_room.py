# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f'{self.name} ({self.height} cm)'
    
class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)

    def is_empty(self):
        if self.people: return False
        else: return True

    def print_contents(self):
        if self.people:
            print(f'There are {len(self.people)} persons in the room, and their combined height is {sum(p.height for p in self.people)} cm')
            for p in self.people: print(p)

    def shortest(self):
        if self.people:
            shortest = min(self.people, key = lambda p: p.height)
            return shortest

    def remove_shortest(self):
        if self.people:
            to_remove_index, remove_obj = min(enumerate(self.people), key = lambda p: p[1].height)
            self.people.pop(to_remove_index)
            return remove_obj
                
        else: return None


if __name__ == '__main__':
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()


    
