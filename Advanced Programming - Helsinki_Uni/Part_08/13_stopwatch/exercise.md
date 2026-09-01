# Stopwatch

## Exercise Brief

The exercise template contains the following skeleton for the Stopwatch class:

class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

Please add to the class definition so that it works as follows:

watch = Stopwatch()
for i in range(3600):
    print(watch)
    watch.tick()

# Sample output:

00:00
00:01
00:02
... 
00:59
01:00
01:01
... 
59:58
59:59
00:00
00:01

So, the method tick adds one second to the stopwatch. The maximum value for both seconds and minutes is 59. 
Your class definition should also contain a __str__ method, which returns a string representation of the state of the stopwatch, as shown in the example above.
