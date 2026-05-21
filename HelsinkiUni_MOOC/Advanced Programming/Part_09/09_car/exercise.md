# Car Task Instructions

Implement a class named `Car` with private (encapsulated) state:

- Amount of petrol in the tank: 0-60 litres
- Odometer reading: in kilometres

Fuel consumption rule:

- The car uses 1 litre of petrol per 1 kilometre driven.

Required methods:

- `fill_up()`
  - Fills the petrol tank to 60 litres.
- `drive(km: int)`
  - Drives for the requested distance if enough petrol is available.
  - If there is not enough petrol, drives only as far as the remaining petrol allows.
- `__str__()`
  - Returns output in this format:
  - `Car: odometer reading X km, petrol remaining Y litres`

Behavior example:

```python
car = Car()
print(car)
car.fill_up()
print(car)
car.drive(20)
print(car)
car.drive(50)
print(car)
car.drive(10)
print(car)
car.fill_up()
car.fill_up()
print(car)
```

Expected output:

```text
Car: odometer reading 0 km, petrol remaining 0 litres
Car: odometer reading 0 km, petrol remaining 60 litres
Car: odometer reading 20 km, petrol remaining 40 litres
Car: odometer reading 60 km, petrol remaining 0 litres
Car: odometer reading 60 km, petrol remaining 0 litres
Car: odometer reading 60 km, petrol remaining 60 litres
```

Encapsulation requirement:

- Petrol amount and odometer reading must not be directly accessible from outside the class.
