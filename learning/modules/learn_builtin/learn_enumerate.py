__author__ = "Saurabh Saxena from 3-Minute Tech"


def what_is_enumerate():
    """
    What is enumerate, a data structure, class, an iterable?. Let's find out
    """
    days_name_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    enumerate_pair = enumerate(days_name_week)

    for value in enumerate_pair:
        print(f'Value: {value}')


def two_breathe_down():
    """
    enumerate() takes an iterable sequence and a returns an enumerator.
    This returns pairs of count and value in the iterable sequence.
    Since it returns a pair, we can individually get both of these
    But how do I get the value from tuple?
    """
    days_name_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for count, value in enumerate(days_name_week):
        print(f'Count: {count} and Value: {value}')


def four_feet_under():
    """
        My friend doesn't understand '0' notation, and Monday is the Day '1' of week! Duuh!

        It's okay I too have such friends and life is funny!
    """

    days_name_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for count, value in enumerate(days_name_week, start=1):
        print(f'Count: {count} and Value: {value}')


def three_feet_under():
    """
        Remember, you can't pass anything which isn't iterable, the object data structure should implement iterable
        """

    is_iterable = 12345
    print(f'Representation: {type(is_iterable)}')

    try:
        enumerate(is_iterable)
    except TypeError as te:
        # Prints: 'int' object is not iterable
        print(te)
    else:
        print('''Ohh gosh I'm iterable''')


def can_iterate_str():
    """
    User to implement the method
    """
    pass


def can_iterate_set():
    """
    User to implement the method
    """
    pass


def can_iterate_dict():
    """
    User to implement the method
    """
    pass


def can_iterate_queue():
    """
    User to implement the method
    """
    pass


def can_iterate_stack():
    """
    User to implement the method
    """
    pass


if __name__ == '__main__':
    # what_is_enumerate()
    # two_breathe_down()
    # three_feet_under()
    four_feet_under()
