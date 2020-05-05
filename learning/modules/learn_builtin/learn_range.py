__author__ = "Saurabh Saxena from 3-Minute Tech"


def what_is_range():
    """
    Used to loop specific number of times from start to stop.
    :return:
    """

    length = 5

    for i in range(length):
        print(f'Index: {i}')


def two_breathe_down():
    """
    Okay hold on, what is start and what is stop?
    Notice it didn't printed 'stop' i.e '5' because stop is exclusive and start is inclusive
    """
    length = 5

    for i in range(0, length):
        print(f'Index: {i}')


def three_feet_under():
    """
    So it's just an iterator which loops fixed number of times, I could just write 'while i < length'!

    Point, but what if you need to have a constant stepper? Your "while" loops needs to be modified?

    Let's see how we do with range

    """

    length = 12
    step = 3

    for i in range(0, length, step):
        print(f'Index: {i}')


def four_feet_under():
    """
    How memory efficient it is to iterate a set, tuple, list etc?

    It just uses three parameters and
    all are 'int'. The parameters under the permissible system 'int' range (based on your 32- or 6- bit machine. Check using sys.maxsize)

    So effectively it just stores start, stop and step, hence doesn't matter what the size of range is

    What else can be done? Slicing, get index of item in range, check if number is in range etc.? Let's check one

    """
    length = 15

    range_elm = range(0, length)

    print(f'Index of 2: {range_elm.index(2)}')
    print(f'Slice from 0 to 4')
    for x in range_elm[0:4]:
        print(f'Sliced items: {x}')


def can_iterate_float_or_double():
    """
    User to implement the method
    """
    pass


def can_use_step_as_float_or_double():
    """
    User to implement the method
    """
    pass


def can_implement_airthmetic_progression_series():
    """
    User to implement the method
    """
    pass


if __name__ == '__main__':
    what_is_range()
    two_breathe_down()
    three_feet_under()
    four_feet_under()
