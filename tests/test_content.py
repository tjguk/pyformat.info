from datetime import datetime


def test_simple():
    """
    # Basic formatting

    Simple positional formatting is probably the most common use-case. Use it
    if the order of your arguments is not likely to change and you only have
    very few elements you want to concatenate.

    Since the elements are not represented by something as descriptive as a
    name this simple style should only be used to format a relatively small
    number of elements.
    """
    old_result = '%s %s' % ('one', 'two', )
    new_result = '{} {}'.format('one', 'two')

    assert old_result == new_result
    assert old_result == 'one two'  # output


def test_simple_2():
    old_result = '%d %d' % (1, 2)
    new_result = '{} {}'.format(1, 2)

    assert old_result == new_result
    assert new_result == "1 2"  # output


def test_simple_3():
    """
    With new style formatting it is possible (and in Python 2.6 even mandatory)
    to give placeholders an explicit positional index.

    This allows for re-arranging the order of display without changing the
    arguments.
    """
    new_result = '{1} {0}'.format('one', 'two')

    assert new_result == 'two one'  # output


def test_string_pad_align():
    """
    # Padding and aligning strings

    By default values are formatted to take up only as many characters as
    needed to represent the content. It is however also possible to define that
    a value should be padded to a specific length.

    Unfortunately the default alignment differs between old and new style
    formatting. The old style defaults to right aligned while for new style
    it's left.

    Align right:
    """
    old_result = '%10s' % ('test', )
    new_result = '{:>10}'.format('test')

    assert old_result == new_result
    assert old_result == '      test'  # output


def test_string_pad_align_2():
    """
    Align left:
    """

    old_result = '%-10s' % ('test', )
    new_result = '{:10}'.format('test')

    assert old_result == new_result
    assert old_result == 'test      '  # output


def test_string_pad_align_3():
    """
    Again new style formatting surpasses the old variant by providing more
    control over how values are padded and aligned.

    You are able to choose the padding character:
    """

    new_result = '{:*<10}'.format('test')

    assert new_result == 'test******'  # output


def test_string_pad_align_4():
    """
    And also center align values:
    """

    new_result = '{:^10}'.format('test')

    assert new_result == '   test   '  # output


def test_string_truncating():
    """
    # Truncating long strings

    Inverse to padding it is also possible to truncate overly long values
    to a specific number of characters.
    """
    old_result = '%5.5s' % ('xylophone', )
    new_result = '{:5.5}'.format('xylophone')

    assert old_result == new_result
    assert old_result == 'xylop'  # output


def test_number():
    """
    # Numbers

    Of course it is also possible to format numbers.

    Integers:
    """
    old_result = '%d' % (42, )
    new_result = '{:d}'.format(42)

    assert old_result == new_result
    assert old_result == '42'  # output


def test_number_2():
    """
    Floats:
    """
    old_result = '%f' % (3.141592653589793, )
    new_result = '{:f}'.format(3.141592653589793)

    assert old_result == new_result
    assert old_result == '3.141593'  # output


def test_number_padding():
    """
    # Padding numbers

    Similar to strings numbers can also be constrained to a specific width.
    """
    old_result = '%4d' % (42, )
    new_result = '{:4d}'.format(42)

    assert old_result == new_result
    assert old_result == '  42'  # output


def test_number_padding_2():
    old_result = '%2.2f' % (3.141592653589793, )
    new_result = '{:2.2f}'.format(3.141592653589793)

    assert old_result == new_result
    assert old_result == '3.14'  # output


def test_number_padding_3():
    old_result = '%04d' % (42, )
    new_result = '{:04d}'.format(42)

    assert old_result == new_result
    assert old_result == '0042'  # output


def test_number_sign():
    """
    # Signed numbers

    By default only negative numbers are prefixed with a sign. This can be
    changed of course.
    """

    old_result = '%+d' % (42, )
    new_result = '{:+d}'.format(42)

    assert old_result == new_result
    assert old_result == '+42'  # output


def test_number_sign_2():
    """
    Use a space character to indicate that negative numbers should be prefixed
    with a minus symbol and a leading space should be used for positive ones.
    """
    old_result = '% d' % (-23, )
    new_result = '{: d}'.format(-23)

    assert old_result == new_result
    assert old_result == '-23'  # output


def test_number_sign_3():
    old_result = '% d' % (42, )
    new_result = '{: d}'.format(42)

    assert old_result == new_result
    assert old_result == ' 42'  # output


def test_number_sign_4():
    """
    New style formatting is also able to control the position of the sign
    symbol relative to the padding.
    """

    new_result = '{:=5d}'.format(-23)

    assert new_result == '-  23'  # output


def test_named_placeholders():
    """
    # Named placeholders

    Both formatting styles support named placeholders.
    """
    data = {
        'first': 'Hodor',
        'last': 'Hodor!',
    }

    old_result = '%(first)s %(last)s' % data
    new_result = '{first} {last}'.format(**data)

    assert old_result == new_result
    assert old_result == 'Hodor Hodor!'  # output


def test_named_placeholders_2():
    """
    `.format()` also accepts keyword arguments.
    """

    new_result = '{first} {last}'.format(first="Hodor", last="Hodor!")

    assert new_result == 'Hodor Hodor!'  # output


def getitem_and_getattr():
    """
    # Getitem and Getattr

    New style formatting allows even greater flexibility in accessing nested
    data structures.

    It supports accessing containers that support `__getitem__` like for
    example dictionaries and lists:

    """
    person = {
        'first': 'Jean-Luc',
        'last': 'Picard',
    }

    new_result = '{p[first]} {p[last]}'.format(p=person)

    assert new_result == 'Jean-Luc Picard'  # output


def getitem_and_getattr_2():
    data = [4, 8, 15, 16, 23, 42]

    new_result = '{d[4]} {d[5]}'.format(d=data)

    assert new_result == '23 42'  # output


def getitem_and_getattr_3():
    """
    As well as accessing attributes on objects via `getattr()`:
    """

    class Plant(object):
        type = "tree"

    new_result = '{p.type}'.format(p=Plant())

    assert new_result == 'tree'  # output


def getitem_and_getattr_4():
    """
    Both type of access can be freely mixed and arbitrarily nested:
    """

    class Plant(object):
        type = "tree"
        kinds = [{
            'name': "oak",
        }, {
            'name': 'maple'
        }]

    new_result = '{p.type}: {p.kinds[0].name}'.format(p=Plant())

    assert new_result == 'tree: oak'  # output


def test_datetime():
    """
    # Datetime values

    Additionally new style formatting allows objects to control their own
    rendering via the `__format__()` magic method. This for example allows
    datetime objects to be formatted inline.
    """

    from datetime import datetime

    new_result = '{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5))

    assert new_result == '2001-02-03 04:05'  # output
