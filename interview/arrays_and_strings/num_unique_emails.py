class Solution:
    def numUniqueEmails(self, emails: [str]) -> int:
        answers = set()
        for email in emails:
            aux = []
            index = 0
            search = True
            index_at = self.find_char(email, index)
            while index <= len(email)-1:
                letter = email[index]
                if letter == '.' and index < index_at:
                    index += 1
                    continue
                if letter == '+' and search:
                    index = index_at
                    search = False
                    continue
                aux.append(letter)
                index += 1
            answers.add(''.join(aux))
        print(answers)
        return len(answers)

    def find_char(self, string: str, start: int, char='@') -> int:
        """
        Used to find the position of
        """
        for i in range(start, len(string) - 1):
            if string[i] == '@':
                return i


if __name__ == '__main__':
        sol = Solution()
        ans = sol.numUniqueEmails(emails=["test.email+alex@leetcode.com", "test.email@leetcode.com"])
        print(ans)