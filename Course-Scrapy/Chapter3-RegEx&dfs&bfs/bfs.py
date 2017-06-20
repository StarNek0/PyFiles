# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/6/20 16:52'


def level_queue(root):  # 二叉树的广搜队列实现
    if root is None:
        return
    my_queue = []
    node = root
    my_queue.append(node)  # node传入队列
    while my_queue:  # 队列不为空
        node = my_queue.pop(0)  # 弹出值
        print node.item
        if node.lchild is not None:
            my_queue.append(node.lchild)
        if node.rchild is not None:
            my_queue.append(node.rchild)
