class Solution:
    def concatHex36(self, n: int) -> str:
        def to_base(num, base):
            if num == 0:
                return '0'
            digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            result = ''
            while num:
                result = digits[num % base] + result
                num //= base
            return result
        
        hex_val = to_base(n * n, 16)
        hex36_val = to_base(n * n * n, 36)
        return hex_val + hex36_val