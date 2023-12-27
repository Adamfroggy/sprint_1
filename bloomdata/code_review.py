'''
MODULE DOCSTRING
'''

import math
import sys


def example1():
    """
    FUNCTION DOCSTRING
    This is a long comment and
    should be wrapped to fit within a 72-character limit.
    """
    some_tuple = (1, 2, 3, 'a')
    some_variable = {
        "long": ('Code should be wrapped within 79 characters to prevent '
                 'page cutoff stuff'),
        "other": [math.pi, 100, 200, 300, 9999292929292]
                ("This is a long string and goes beyond what it should"),
        "more": {"inner": "THIS whole logical line should be wrapped"},
        "data": [444, 5555, 222, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    }
    return some_tuple, some_variable


def example_2():
    '''
    FUNCTION DOCSTRING
    '''
    return {"has_key() is deprecated": True}


class Example3():
    def __init__(self, bar):
        self.some_value = self._calculate_value(bar)

    def _calculate_value(self, bar):
        '''
        METHOD DOCSTRING
        '''
        if bar:
            bar += 1
            bar = bar * bar
            return bar
        else:
            some_string = """
            INDENTATION IN STRINGS SHOULD NOT BE TOUCHED'
            only actual code should be reindented,
            THIS IS MORE CODE
            """
            return (sys.path, some_string)
