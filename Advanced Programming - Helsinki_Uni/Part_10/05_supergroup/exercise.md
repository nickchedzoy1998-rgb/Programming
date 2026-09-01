# Supergroup

The exercise template contains the class definition for a `SuperHero`.

Define a class named `SuperGroup` which represents a group of superheroes. The
class should contain the following members:

- Protected attributes `name` (`str`), `location` (`str`) and `members`
  (`list`).
- A constructor which takes the name and location of the group as arguments,
  in that order.
- Getter methods for the `name` and `location` attributes.
- A method named `add_member(hero: SuperHero)` which adds a new member to the
  group.
- A method named `print_group()` which prints information about the group and
  its members in the format specified below.

## Example

```python
superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
invisible = SuperHero("Invisible Inca", "Invisibility")
revengers = SuperGroup("Revengers", "Emerald City")

revengers.add_member(superperson)
revengers.add_member(invisible)
revengers.print_group()
```

## Sample output

```text
Revengers, Emerald City
Members:
SuperPerson, superpowers: Superspeed, superstrength
Invisible Inca, superpowers: Invisibility
```
