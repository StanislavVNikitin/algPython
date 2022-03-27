##1. Реализовать параллельную обработку пакетов
##Условие здесь: https://stepik.org/media/attachments/lesson/41233/statements.pdf
##Сдавать здесь: https://stepik.org/course/1547/syllabus раздел 2.3 вторая задача, на курсе нужно зарегистрироваться.

# 1 Задачу к сожалению не смог решить, было бы интересено посмотреть вариант решения.

###Доп задачи на деревья:
###Усложненная версия задачи с урока: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        que = collections.deque([root])
        while que:
            size = len(que)
            for i in range(size):
                node=que.popleft()
                if i<size-1:
                    node.next=que[0]
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return root 
    




###Найти самого низкого общего родителя: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if  root == None or root == p or root == q :
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        print(root.val,left, right)
        return left if left  else right