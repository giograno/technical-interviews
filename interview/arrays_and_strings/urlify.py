import unittest


def urlify(my_string, true_len):
    """
    URLify
    @chapter 11
    @exercise 1.3
    @page 90
    Write a method to replace all spaces in a string with '%20'. You might assume the string has sufficient space
    at the end to hold additional characters and that you are given the true len of the string.
    """
    space_counts = 0
    for elem in my_string:
        if elem == ' ':
            space_counts += 1

    index = true_len + space_counts * 2
    print(index)
    for i in reversed(range(0, true_len-1)):
        print(i)
        if my_string[i] == ' ':
            my_string[index-1] = '0'
            my_string[index-2] = '2'
            my_string[index-3] = '%'
            index -= 3
        else:
            my_string[index-1] = my_string[i]
            index -= 1

    return my_string


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertTrue(urlify(list('Mr John Smith    '), 13) == "Mr%20John%20Smith")


if __name__ == '__main__':
    unittest.main()



