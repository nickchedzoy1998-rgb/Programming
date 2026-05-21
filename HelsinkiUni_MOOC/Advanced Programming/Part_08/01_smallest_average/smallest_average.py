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

if __name__ == '__main__':
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))