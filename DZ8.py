### Одна задача на структуру данных "Непересекающиеся множества", рассмотренную на уроке.
### https://leetcode.com/problems/number-of-operations-to-make-network-connected/
###
### Решение сам не осилил, нашел в интернете, оно мне показалось оптимальным. Но мне еще конечно учится и учится! 
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        p = {x : x for x in range(n)}
        def find(x):
            while x != p[x]:
                p[x] = p[p[x]]
                x = p[x]
            return x
           
        for x, y in connections:
            p[find(x)] = find(y)
        
        return len({find(x) for x in range(n)}) - 1