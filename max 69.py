class Solution:
    def maximum69Number(self, num: int) -> int:
        strNum = list(str(num))
        for i in range(len(strNum)):
            if strNum[i] == '6':
                strNum[i] = '9'
                break
        return int(''.join(strNum))