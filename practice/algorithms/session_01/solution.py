"""Session 01: longest contiguous substring with no repeated characters."""


def longest_unique_substring(text: str) -> int:
    """Return the length of the longest substring with no repeated characters."""
    text_length = len(text)

    if text_length == 0 or text_length == 1:
        return text_length
    
    longest_substring = 1
    skip_to_index = 0

    for i, char in enumerate(text):
        substring = {}
        repeated = False

        if i < skip_to_index:
            continue

        substring[char] = i
        next = i

        while repeated == False and next <= text_length-2:
            next += 1

            if text[next] not in substring.keys():
                substring[text[next]] = next
                if len(substring.keys()) > longest_substring:
                    longest_substring = len(substring.keys())

            else:
                repeated = True
                skip_to_index = substring[text[next]] + 1
                
    return longest_substring


# The challenge: Longest substring without repeating characters
# Write a Python function that returns the length of the longest contiguous substring containing no repeated characters.
    # Input	Expected output
        # "abcabcbb"	3
        # "bbbbb"	1
        # "pwwkew"	3
        # ""	0
    # For example, "abcabcbb" contains "abc", which is three characters long with no repetitions.


if __name__ == '__main__':
    print(longest_unique_substring('abcabcbb'))
    print(longest_unique_substring('bbbb'))
    print(longest_unique_substring('pwwkew'))
    print(longest_unique_substring(''))