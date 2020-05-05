__author__ = "Saurabh Saxena from 3-Minute Tech"


def what_is_zip():
    number_of_days = [1, 2, 3, 4, 5, 6, 7]
    days_in_a_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for day, name in zip(number_of_days, days_in_a_week):
        print(f'Day: {day} and Name: {name}')


def two_breathe_down():
    """
    Now the length of both data structure is different. Will it error-out while iterating?
    Also did you noticed, that both have different data type?
    """
    number_of_days = [1, 2, 3, 4, 5, 6]
    days_in_a_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for day, name in zip(number_of_days, days_in_a_week):
        print(f'Day: {day} and Name: {name}')


def three_feet_under():
    """
        Well essentially it returns Tuple, since it just takes an iterable as an input

        Try using three Iterables.

        And yes, remember don't believe what I say!

        """
    number_of_days = [1, 2, 3, 4, 5, 6, 7]
    days_in_a_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    zipped_tuple = zip(number_of_days, days_in_a_week)

    print(f'Representation: {list(zipped_tuple)}')
    print(f'''What's my Type? : {type(zipped_tuple)} and I belong to: {type(zipped_tuple).__module__}!''')


if __name__ == '__main__':
    # what_is_zip()
    # print('Executing two_breathe_down')
    # two_breathe_down()
    three_feet_under()