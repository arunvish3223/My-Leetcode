class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set(deadends)
        if "0000" in visit:
            return -1
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1+10) % 10) 
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        q = deque([("0000", 0)])
        while q:
            lock, turn = q.popleft()
            if lock == target:
                return turn
            for child in children(lock):
                if child not in visit:
                    q.append((child, turn + 1)) 
                    visit.add(child)
        return -1
