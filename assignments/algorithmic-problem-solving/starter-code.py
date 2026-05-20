"""Starter code for Algorithmic Problem Solving.

Students will practice two challenges:
1) Word frequency counting with dictionaries
2) Pair-sum (two-sum) with loops vs dictionary lookups
"""


def count_word_frequencies(words):
    """Return a dictionary mapping each word to its frequency."""
    frequencies = {}
    # TODO: Count each word using a dictionary.
    return frequencies


def top_n_words(frequencies, n=3):
    """Return the top n words sorted by highest frequency."""
    # TODO: Return a list of (word, count) tuples.
    return []


def two_sum_bruteforce(nums, target):
    """Find indices of two numbers that add to target using nested loops."""
    # TODO: Implement O(n^2) solution.
    return None


def two_sum_dict(nums, target):
    """Find indices of two numbers that add to target using a dictionary."""
    # TODO: Implement near O(n) solution.
    return None


def main():
    words = [
        "python",
        "api",
        "python",
        "list",
        "dict",
        "python",
        "dict",
        "loop",
        "api",
        "dict",
    ]

    nums = [2, 7, 11, 15]
    target = 9

    frequencies = count_word_frequencies(words)
    print("Word frequencies:", frequencies)
    print("Top words:", top_n_words(frequencies, n=3))

    print("Two-sum brute force:", two_sum_bruteforce(nums, target))
    print("Two-sum dictionary:", two_sum_dict(nums, target))


if __name__ == "__main__":
    main()
