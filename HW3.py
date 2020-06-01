def words_containing(sentence, letter):
    """ Given a sentence, returns list of words that contain the letter.
        Letter given is lowercase. Sentence can be mixed case, and the
        case should be ignored for searching.
    """
    words = sentence.split()
    return [
        word
        for word in words
        if letter in word.lower()
    ]


def len_safe(object):
    """Return length of object or -1 if object has no length."""
    try:
        return len(object)
    except TypeError:
        return -1


def unique(sequence):
    """Yield sequence elements in order, skipping duplicate values."""
    seen_items = set()
    for item in sequence:
        if item not in seen_items:
            seen_items.add(item)
            yield item


def unique2(sequence):
    """Yield sequence elements in order, skipping duplicate values."""
    for index, item in enumerate(sequence):
        if item not in sequence[:index]:
            yield item


def unique3(sequence):
    """Yield sequence elements in order, skipping duplicate values."""
    return (
        item
        for index, item in enumerate(sequence)
        if item not in sequence[:index]
    )


def unique4(sequence):
    """Yield iterable elements in order, skipping duplicate values."""
    yield from dict.fromkeys(sequence)
