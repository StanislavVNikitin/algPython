### Реализовать обход дерева post-order. Сначала левое, потом правое поддерево, в последнюю очередь корень: 
### https://leetcode.com/problems/binary-tree-postorder-traversal/

class Solution:
  def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ans = []

    def postOrder(root: Optional[TreeNode]) -> None:
      if not root:
        return

      postOrder(root.left)
      postOrder(root.right)
      ans.append(root.val)

    postOrder(root)
    return ans


### Проверить дерево на симметричность: 
### https://leetcode.com/problems/symmetric-tree/

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:        
        def isMirror(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right: return True
            if not left or not right: return False
            if left.val != right.val: return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        return isMirror(root, root)    
