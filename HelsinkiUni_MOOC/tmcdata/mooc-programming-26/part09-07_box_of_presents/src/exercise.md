# A Box of Presents

In this exercise you will practice wrapping presents. You will write two classes: `Present` and `Box`. A present has a name and a weight, and a box contains presents.

## The Present Class

Please define the class `Present` which can be used to represent different kinds of presents. The class definition should contain attributes for the name and the weight (in kg) of the present. 

Instances of the class should work as follows:

```python
book = Present("ABC Book", 2)

print("The name of the present:", book.name)
print("The weight of the present:", book.weight)
print("Present:", book)
```

**Expected Output:**
```
The name of the present: ABC Book
The weight of the present: 2
Present: ABC Book (2 kg)
```

## The Box Class

Please define the class `Box`. You should be able to add presents to the box, and the box should keep track of the combined weight of the presents within. 

### Required Methods:

- `add_present(self, present: Present)` - Adds the present given as an argument to the box. The method has no return value.
- `total_weight(self)` - Returns the combined weight of the presents in the box.

### Example Usage:

```python
book = Present("ABC Book", 2)

box = Box()
box.add_present(book)
print(box.total_weight())

cd = Present("Pink Floyd: Dark Side of the Moon", 1)
box.add_present(cd)
print(box.total_weight())
```

**Expected Output:**
```
2
3
```