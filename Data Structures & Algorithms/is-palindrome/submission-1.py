class Solution:
    def isPalindrome(self, s: str) -> bool:
        charlist="0123456789abcdefghijklmnopqrstuvwxyz"
        new_s=""
        for i in s:
            if i.lower() in charlist:
                new_s+=i.lower()
        print(new_s)
        if new_s[::-1]==new_s:
            return True
        return False

        