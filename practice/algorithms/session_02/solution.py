"""Algorithm exercise 02: shortest qualifying contiguous segment."""


def min_subarray_length(target: int, numbers: list[int]) -> int:
    """Return shortest contiguous subarray length with sum >= target, or 0."""
    if any(number >= target for number in numbers):
        return 1
    
    if target-1 in numbers and len(numbers) > 1:
        return 2
    
    shortest_array = 0
    start = 0

    for end, num in enumerate(numbers):
        sub_array = numbers[start: end+1]
        total = sum(sub_array)

        if total < target:
            continue

        else:
            while total >= target and len(sub_array) > 1:
                if shortest_array == 0:
                    shortest_array = len(sub_array)
                else:
                    if len(sub_array) < shortest_array:
                        shortest_array = len(sub_array)

                start += 1
                sub_array = sub_array[1:]
                total = sum(sub_array)

    return shortest_array


            


