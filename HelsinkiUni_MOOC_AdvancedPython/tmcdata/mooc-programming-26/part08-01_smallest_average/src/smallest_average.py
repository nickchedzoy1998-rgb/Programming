### SMALLEST AVERAGE RESULT ###

"""
Please write a function named smallest_average(person1: dict, person2: dict, person3: dict), which takes three dictionary objects as its arguments.

Each dictionary object contains values mapped to the following keys:

"name": The name of the contestant
"result1": the first result of the contestant (an integer between 1 and 10)
"result2": the second result of the contestant (as above)
"result3": the third result of the contestant (as above)
The function should calculate the average of the three results for each contestant, and then return the contestant whose average result was the smallest. The return value should be the entire dictionary object containing the contestant's information.

You may assume there will be no ties, i.e. a single contestant will have the smallest average result.

Example Variables:
person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

"""

# SOLUTION

def smallest_average(person1:  dict, person2: dict, person3: dict):

    def get_sum(person):
        return(person['result1'] + person['result2'] + person['result3'])
    
    people = [person1, person2, person3]
    low_sum = get_sum(people[0])
    low_score = people[0]

    for p in people:
        current_sum = get_sum(p)

        if current_sum < low_sum:
            low_sum = current_sum
            low_score = p

    return low_score