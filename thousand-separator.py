class Solution:
    def thousandSeparator(self, n: int) -> str:
        ret_str = ''
        count = 0
        for i in str(n)[::-1]:
            if not count%3 and count:
                print(count)
                ret_str += '.'
            ret_str += i
            count += 1
        return ret_str[::-1]
