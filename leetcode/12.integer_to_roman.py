class Solution:

    def intToRoman2(self, num):
        d = [
            [1000, 'M'],
            [900, 'CM'],
            [500, 'D'],
            [400, 'CD'],
            [100, 'C'],
            [90, 'XC'],
            [50, 'L'],
            [40, 'XL'],
            [10, 'X'],
            [9, 'IX'],
            [5, 'V'],
            [4, 'IV'],
            [1, 'I']
        ]
        roman = ''
        for i in d:
            roman += (num//i[0]) * i[1]
            num = num % i[0]
        return roman

    def intToRoman(self, num: int) -> str:
        if num > 3999 or num == 0:
            return
        roman_reff = {
            1:'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }
        decimal_place = ''
        all_num = []
        while num > 0:
            remainder = [num % 10]
            place = int('1'+decimal_place)
            if 0 < remainder[0] < 4:
                remainder = [roman_reff[1*place] for _ in range(0, remainder[0])] 
            elif remainder[0] == 4:
                remainder = [roman_reff[1*place], roman_reff[5*place]]
            elif remainder[0] == 5:
                remainder = [roman_reff[5*place]]
            elif 5 < remainder[0] < 9:
                remainder = [roman_reff[5*place]] + [roman_reff[1*place] for _ in range(0, remainder[0]-5)]
            elif remainder[0] == 9:
                remainder = [roman_reff[1*place], roman_reff[10*place]]
            else:
                remainder = []
            all_num = remainder + all_num

            num = num // 10
            decimal_place += '0'
        return ''.join(all_num)

if __name__ == '__main__':
    s = Solution()
    s.a(3825)
    # s.intToRoman(31)
    # s.intToRoman(32)
    # s.intToRoman(33)
    # s.intToRoman(34)
    # s.intToRoman(35)
    # s.intToRoman(36)
    # s.intToRoman(37)
    # s.intToRoman(38)
    # s.intToRoman(39)
    # s.intToRoman(40)