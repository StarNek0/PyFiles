# coding:utf8
"""
--------------------------------------------------------------------------
    File:   hash_sha512.py
    Auth:   zsdostar
    Date:   2018/4/12 17:12
    Sys:    Windows 7
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""
__author__ = 'zsdostar'

import hashlib


def hyashi(pwd, wheels=0):
    """
    hyashi could hash any times for your request, however 500000 times may spend 1s, it's linear relation of time and times.
    :param pwd: request password.
    :param wheels: sha512 times.
    :return: result after hyashi() the pwd for wheels times.
    """
    pwd = hashlib.sha512(pwd).hexdigest()
    if not wheels:
        return pwd
    for _ in xrange(wheels):
        pwd = hashlib.sha512(pwd).hexdigest()
    return pwd


if __name__ == '__main__':
    print hyashi('', 25000)
