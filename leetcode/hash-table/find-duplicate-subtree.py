from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        if root is None:
            return []
        res = []
        hash_map = {}
        stack = []
        while len(stack) != 0 or root is not None:
            while root is not None:
                stack.append(root)
                # 序列化树
                root_ser = self.serialize(root)
                # 查看是否在hash_map中，如果不在就加入，如果在就append， 但是只应该append一次
                if root_ser not in hash_map.keys():
                    hash_map[root_ser] = 1
                elif hash_map[root_ser] == 1:
                    res.append(root)
                    hash_map[root_ser] += 1
                root = root.left
            node = stack.pop()
            root = node.right
        return res

    def serialize(self, root):
        if root is None:
            return "#"
        left_ser = self.serialize(root.left)
        right_ser = self.serialize(root.right)
        return str(root.val) + "," + left_ser + "," + right_ser
