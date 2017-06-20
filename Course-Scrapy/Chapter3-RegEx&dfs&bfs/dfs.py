# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/20 16:34'


def depth_tree(tree_node):  # 二叉树的深搜模型
    if tree_node is not None:
        print (tree_node._data)
        if tree_node._left is not None:
            return depth_tree(tree_node._left)
        if tree_node._right is not None:
            return depth_tree(tree_node._right)
