# coding:utf8
"""
--------------------------------------------------------------------------
    File:   补充缺失的代码.py
    Auth:   zsdostar
    Date:   2018/1/11 19:38
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""


def print_directory_contents(sPath):
    """
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。

    """
    # 补充代码
    import os

    for dir_child in os.listdir(sPath):  # listdir 返回目录下所有文件和子目录
        child_path = os.path.join(sPath, dir_child)  # 将目录与其子目录/文件拼接起来
        if os.path.isdir(child_path):
            print_directory_contents(child_path)
        else:
            print(child_path)


# print_directory_contents('')
