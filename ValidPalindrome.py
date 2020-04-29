s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            while not s[left].isalpha():
                left += 1
            while not s[right].isalpha():
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

print(isPalindrome(s))
