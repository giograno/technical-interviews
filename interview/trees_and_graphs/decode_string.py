import unittest


def decode_string(s: str) -> str:

    ans = []
    i = 0
    j = 0
    while i < len(s)-1:
        if s[i].isdigit():
            j += 2
            character = s[j]
            temp = []
            while character != ']':
                temp.append(character)
                j += 1
                character = s[j]
            ans.extend(int(s[i]) * temp)
            j += 1
            i = j
        else:
            ans.append(s[i])
            i += 1
            j += 1
    return ''.join(ans)


class TestSolution(unittest.TestCase):

    def test_solution(self):
        ans = decode_string('3[a]2[bc]')
        self.assertTrue('aaabcbc' == ans)

    def test_solution2(self):
        ans = decode_string('3[a2[c]]')
        self.assertTrue('accaccacc' == ans)

    def test_solution3(self):
        ans = decode_string('2[abc]3[cd]ef')
        self.assertTrue('abcabccdcdcdef' == ans)


if __name__ == '__main__':
    unittest.main()
