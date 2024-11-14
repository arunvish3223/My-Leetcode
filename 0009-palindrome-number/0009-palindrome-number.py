class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        ans=0
        while x>0:
            d=x%10
            ans=(ans*10)+d
            x=x//10
        return ans==y

        