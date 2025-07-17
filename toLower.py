class Solution:
    def toLowerCase(self, s):
        result = ""
        for ch in s:
            if 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)
            else:
                result += ch
        return result
