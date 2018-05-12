# coding:utf8
"""
--------------------------------------------------------------------------
    File:   ShowAvatarByEmail.py
    Auth:   zsdostar
    Date:   2018/4/12 12:00
    Sys:    Windows 7
--------------------------------------------------------------------------
    Desc:   如果是gravatar的用户，那么得到他的邮箱名即可得到他的头像，原理
            是gravatar为每个邮箱计算md5哈希值作为该邮箱的头像url的后半部分
--------------------------------------------------------------------------
"""
import hashlib


def get_avatar(email=u'zsdzzydos@gmail.com', size=300):
    """ Give an true email address and return the avatar image source url of the email.
        You should register your email at http://www.gravatar.com/ .
            :param email : The email address given.
            :param size : The avatar size.
            :returns gravatar_url : The avatar image source url.
    """
    gravatar_url = u'http://www.gravatar.com/avatar/'
    return gravatar_url + hashlib.md5(email).hexdigest() + '?s=' + str(size)


if __name__ == '__main__':
    print(get_avatar())
