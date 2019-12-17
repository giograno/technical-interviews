# Given two strings, write a method that decides if one is a permutation of the other
 

def sort_permutation(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    return sorted(string_a) == sorted(string_b)


def smart_permutation(string_a, string_b):
    if len(string_a) != len(string_b):
        return False

    counter = [0] * 128
    for elem in string_a:
        val = ord(elem)
        counter[val] += 1

    for elem in string_b:
        val = ord(elem)
        counter[val] -= 1
        if counter[val] < 0:
            return False

    return True
    


if __name__ == '__main__':
    res = sort_permutation('ciao', 'oiac')
    assert res == True
    res = sort_permutation('ciao', 'ciap')
    assert res == False
    res = smart_permutation('ciao', 'oiac')
    assert res == True
    res = smart_permutation('ciao', 'ciap')
    assert res == False
