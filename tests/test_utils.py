import pytest

import cool.utils

argvalues = []
argvalues.append([[], []])
argvalues.append([{'a': None}, []])
argvalues.append([None, []])
argvalues.append([['a', 'b', 'c'], [('', 'a'), ('', 'b'), ('', 'c')]])
argvalues.append([[{'a': 0}, {'b': 1}], [('[a]', 0), ('[b]', 1)]])
argvalues.append([{'c': [{'a': 0}, {'b': 1}]}, [('c[][a]', 0), ('c[][b]', 1)]])
argvalues.append([{'a': [], 'b': [None, None, {'c': None}]}, []])
argvalues.append(['a', [('', 'a')]])
argvalues.append([{'a': 0, 'b': 1}, [('a', 0), ('b', 1)]])
argvalues.append([{'a': True, 'b': False}, [('a', 'true'), ('b', 'false')]])
argvalues.append([[('a', 0), ('b', 1)], [('a', 0), ('b', 1)]])
argvalues.append([{'a': [0, 1, 2]}, [('a[]', 0), ('a[]', 1), ('a[]', 2)]])
argvalues.append([{'a': [('b', 0), ('c', 1)]}, [('a[b]', 0), ('a[c]', 1)]])
argvalues.append([{
    'a': [('b', [0, 1]), ('c', [1, 2])]
}, [('a[b][]', 0), ('a[b][]', 1), ('a[c][]', 1), ('a[c][]', 2)]])
argvalues.append([{
    'a': [('b', [0, None]), ('c', [1, 2])]
}, [('a[b][]', 0), ('a[c][]', 1), ('a[c][]', 2)]])
argvalues.append([{'a': {'b': {'c': 0}}}, [('a[b][c]', 0)]])
argvalues.append([[('a', [('b', [('c', 0)])])], [('a[b][c]', 0)]])
argvalues.append([[('a', [('b', [('c', None)])])], []])
argvalues.append([{'include': [('', 0), ('', 1)]}, [('include[]', 0), ('include[]', 1)]])


@pytest.mark.parametrize('test_input,expected', argvalues)
def test_resolve_query(test_input, expected):
    params = cool.utils.resolve_query(test_input)
    assert params == expected
    assert cool.utils.resolve_query(params) == params
