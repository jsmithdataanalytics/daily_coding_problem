
def longest_substring_of_k_distinct_characters(string, k):
    longest = 0

    for start, start_char in enumerate(string):
        distinct_chars, num_distinct_chars = set(), 0

        for end, end_char in enumerate(string):

            if end < start:
                continue

            if end_char not in distinct_chars:
                distinct_chars.add(end_char)
                num_distinct_chars += 1

                if num_distinct_chars > k:
                    break

            longest = max(longest, end - start + 1)

    return longest


if __name__ == '__main__':
    assert longest_substring_of_k_distinct_characters('abcba', 2) == 3
    assert longest_substring_of_k_distinct_characters('kghshgkre', 3) == 5
