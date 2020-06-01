""" CLI program answers to test HW3 homework """
# Diane Chen

import argparse
from HW3 import words_containing, len_safe, unique


def test_words_containing():
    """Return True/False if the test of words_containing passes/fails"""
    # Test 1 make sure it matches upper and lower case
    sentence = "The cow jumped over the moon"
    result = words_containing(sentence, 't')
    expected = ['The', 'the']
    if result != expected:
        return False

    # Test 2 make sure it gets all the words
    expected = ['cow', 'over', 'moon']
    result = words_containing(sentence, 'o')
    if result != expected:
        return False

    # Test 3 Return empty string if no matches
    expected = []
    result = words_containing(sentence, 'x')
    if result != expected:
        return False

    # Test 4 No error if sentence is empty
    if words_containing('', 'a') != []:
        return False

    # All tests passed if we get here
    return True


def test_len_safe():
    """Return True/False if the test of len_safe passes/fails"""
    # Test 1, dictionary with 2 entries
    my_dict = {'a': 23, 'b': 8}
    result = len_safe(my_dict)
    if result != 2:
        return False

    # Test 2, integer should return -1
    result = len_safe(7)
    if result != -1:
        return False

    # Test 3, empty list, should return 0
    result = len_safe([])
    if result != 0:
        return False

    # All tests passed if we get here
    return True


def test_unique():
    """Return True/False if the test of unique passes/fails"""
    numbers = [4, 5, 2, 6, 7, 2, 3, 5, 8]
    expected = [4, 5, 2, 6, 7, 3, 8]
    # Save the results from calling next.
    result = []
    nums = unique(numbers)
    # We know there should be 7 numbers, so call next() 7 times to get them.
    # Save them to compare later.
    # Use a try/except just in case something goes wrong and we get a
    #   StopIteration error too early.
    try:
        result.append(next(nums))
        result.append(next(nums))
        result.append(next(nums))
        result.append(next(nums))
        result.append(next(nums))
        result.append(next(nums))
        result.append(next(nums))
    except StopIteration:
        # We shouldn't get any exceptions here
        return False

    # We should have all the numbers in the result list at this point.
    # This call to next() should raise a StopIteration error.
    try:
        next(nums)
    except StopIteration:
        # Done, so now verify that the numbers we got back are correct.
        if result != expected:
            return False
    else:
        # We shouldn't get here if things work correctly.
        return False

    # Test 2, try with empty list
    nums = unique([])
    # Should get error first time.
    try:
        next(nums)
    except StopIteration:
        # Nothing to do here, since this is what we want to happen.
        # Use pass to continue in case we add more tests after this one.
        # (Rather than return True here, which would be OK,
        # but I like having only one place for return True at the end.)
        pass
    else:
        # We shouldn't get here if things work correctly.
        return False

    # All tests passed if we get here
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-w',
        '--words',
        action='store_true',
        help='Flag to test the words_containing function from HW3'
    )
    parser.add_argument(
        '-l',
        '--len',
        action='store_true',
        help='Flag to test the len_safe function from HW3'
    )
    parser.add_argument(
        '-u',
        '--unique',
        action='store_true',
        help='Flag to test the unique function from HW3'
    )
    # I often rely on "truthiness", but for testing, it's sometimes better
    # to be explicit, rather than relying on implicit values.
    # A test function might return something that isn't True or False,
    # when only True/False are valid. Truthiness testing won't catch that.
    args = parser.parse_args()
    if args.words:
        result = test_words_containing()
        if result is True:
            print("words_containing passed")
        else:
            print("words_containing failed")

    if args.len:
        if test_len_safe() is True:
            print("len_safe passed")
        else:
            print("len_safe failed")

    if args.unique:
        if test_unique() is True:
            print("unique passed")
        else:
            print("unique failed")
