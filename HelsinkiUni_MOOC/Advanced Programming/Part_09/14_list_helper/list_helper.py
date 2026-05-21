# WRITE YOUR SOLUTION HERE:

class ListHelper:

    @staticmethod
    def greatest_frequency(my_list: list):
        unique_items = list(set(my_list))

        item_counts = {}

        for item in unique_items:
            count = 0

            for i in my_list:
                if item == i:
                    count += 1

            item_counts[item] = count
        
        max_val = max(item_counts.values())

        max_keys = []

        for key, val in item_counts.items():
            if val == max_val:
                return key
        
        return max_keys
    
    
    @staticmethod
    def doubles(my_list: list):
        unique = list(set(my_list))

        doubles = []

        for i in unique:
            if i not in doubles:
                count = 0
                for n in my_list:
                    if n == i:
                        count += 1

                    if count == 2:
                        doubles.append(i)
                        break

                if count == 2:
                    pass
        
        return len(doubles)


if __name__ == '__main__':
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]

    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))

