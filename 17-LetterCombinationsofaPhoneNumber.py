class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if digits=='':
            return []
        number=list(phone[digits[0]])
        for d in  digits[1:]:
            number=[old+new for old in number for new in list(phone[d])]
            
        return number