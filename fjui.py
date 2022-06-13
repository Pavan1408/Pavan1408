def test_valid_dictionary_keys():
    test_dict = {}
    test_dict[1] = 1
    test_dict["one"] = "string"
    try:
        key = []
        test_dict[key] = "list"
    except TypeError as te:
        print (te)  #observe the error message.      lists are unhashable
        assert True

    try:
        key = (1,2)
        test_dict[key] = "tuple with immutable elements"
    except TypeError as te:
        print (te)
        assert False # do we reach here?   Noooooooo

    try:
        key = (1, [])
        test_dict[key] = "tuple with mutable element"
    except TypeError as te:
        print (te)
        assert True    #do we reach here?          Yesss

    assert {1: 1, 'one': 'string', (1,2): 'tuple with immutable elements'} == test_dict
test_valid_dictionary_keys()