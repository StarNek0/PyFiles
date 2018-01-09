# coding:utf8
"""
--------------------------------------------------------------------------
    File:   链表.py
    Auth:   zsdostar
    Date:   2018/1/9 19:49
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""

# 单向链表
class Node(object):
    def __init__(self, value, nextnode=None):
        self.value = value
        self._nextnode = nextnode

    def append(self, n):
        if not isinstance(n, Node):
            n = Node(n)
        self._nextnode, n = n, self._nextnode
        self._nextnode._nextnode = n

# 双向链表 树？
class TreeNode:
# 类的结构已经包含了指向关系
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

l1 = TreeNode(0)
l2 = TreeNode(1)
l3 = TreeNode(2)

# 引用表示指向关系
l1.left  = l2
l1.right = l3
