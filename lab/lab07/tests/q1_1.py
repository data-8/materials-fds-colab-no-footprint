OK_FORMAT = True

test = {   'name': 'q1_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> len(ab_test_order) == 6\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.allclose(np.array(ab_test_order)[:3] % 2 == 1, True)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.allclose(np.array(ab_test_order)[3:] % 2 == 0, True)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import hashlib\n'
                                               '>>> def get_hash(num):\n'
                                               '...     """Helper function for assessing correctness."""\n'
                                               '...     return hashlib.md5(str(num).encode()).hexdigest()\n'
                                               '>>> get_hash(np.array(ab_test_order).astype(int))\n'
                                               "'a7196ed0f271c873d9750cb92422d911'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
