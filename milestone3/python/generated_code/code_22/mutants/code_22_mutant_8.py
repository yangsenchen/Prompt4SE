
























import numpy


class Validator:
    def _is_compound_mfr_temperature_tuple(self, value):
        '''Determines whether value is a tuple of the format
        (compound(str), mfr(float), temperature(float)).

        :param value: The value to be tested.

        :returns: True or False'''
        
        if not (type(value) is tuple):
            return False
        elif not (len(value) == 3):
            return False
        elif not (type(value[0]) is str):
            return False
        elif (not (type(value[1]) is float) and \
            not (type(value[1]) is numpy.float64) and \
            not (type(value[1]) is numpy.float32)):
            return False
        elif (not (type(value[2]) is float) and \
            type(value[2]) is numpy.float64 and \
            not (type(value[2]) is numpy.float32)):
            return False
        else:
            return True


def main():
    validator = Validator()
    test_value = ('compound', 1.2, 3.0)
    result = validator._is_compound_mfr_temperature_tuple(test_value)
    print('Is test_value valid? :', result)


if __name__ == '__main__':
    main()