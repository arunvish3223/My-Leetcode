class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        def backtrack(path, index):
            if index == len(s):
                result.append("".join(path))
                return
            
            if s[index].isalpha():
                path.append(s[index].lower())
                backtrack(path, index + 1)
                path.pop()
                
                path.append(s[index].upper())
                backtrack(path, index + 1)
                path.pop()
            else:
                path.append(s[index])
                backtrack(path, index + 1)
                path.pop()

        backtrack([], 0)
        return result