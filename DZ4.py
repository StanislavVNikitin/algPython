### Реализовать структуру данных стэк, который за О(1) выдает минимум в стэке:
### https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        self.stack = []
       

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


###Написать код для задачи: "Обработка сетевых пакетов", которую обсудили в конце семинара, условие здесь:
###https://stepik.org/media/attachments/lesson/41233/statements.pdf
###Сдавать задачу здесь:
###https://stepik.org/lesson/41234/step/3?unit=19818
###


from collections import deque
def netstack():
    size, n = map(int, input().split())
    que = deque()
    output = ""

    for i in range(n):
        arrival, dur = map(int, input().split())
        while que and que[0] <= arrival:
            que.popleft()
                
        if len(que) < size:
            if que:
                arrival = max(arrival, que[-1])
            output =f'{output} {arrival}'
            que.append(arrival + dur)
        else:
            output += " -1"
            
    print(output)
        
  

# netstack()
  
