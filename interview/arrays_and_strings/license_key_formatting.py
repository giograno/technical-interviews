class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        valid = 0
        last_valid = 0
        ans = []
        for i, el in enumerate(S):
            if el.isalnum():
                valid += 1
                last_valid = i
        first_size = valid % K

        index = 0
        count = 0
        while count != first_size:
            if S[index].isalnum():
                ans.append(S[index].upper())
                count += 1
            index += 1

        if valid > first_size and count > 0:
            ans.append('-')

        count = 0
        while index < len(S):
            if count % K == 0 and count != 0 and index <= last_valid:
                ans.append('-')
                count = 0
            if S[index].isalnum():
                ans.append(S[index].upper())
                count += 1
            index += 1
        return ''.join(ans)


if __name__ == '__main__':
    sol = Solution()
    ans = sol.licenseKeyFormatting("--a-a-a-a-", 1)
    print(ans)