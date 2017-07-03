# -*- coding:utf-8 -*-


class Lab(object):
    """ \u5b9e\u9a8c
    """

    def __init__(self, name, tags=[]):
        self.name = name
        # FIXME
        self._tags = tags

    def insert_tag(self, tag):
        """ \u63d2\u5165\u6807\u7b7e\uff0c\u9700\u8981\u68c0\u67e5\u6807\u7b7e\u662f\u5426\u5b58\u5728
        """
        # FIXME
        if tag:
            if tag not in self._tags:
                self._tags.append(tag)

    @property
    def tags(self):
        return self._tags

    def can_be_started(self, user):
        """\u5224\u65ad\u7528\u6237\u80fd\u5426\u542f\u52a8\u5b9e\u9a8c\uff0c\u53ea\u6709\u767b\u5f55\u7684\u4f1a\u5458\u7528\u6237\u624d\u80fd\u542f\u52a8\u5b9e\u9a8c
        """
        # FIXME
        if not user.is_authenticated():
            can = False
            return can
        elif user.is_member():
            can = True
            return can
if __name__ == '__main__':
    lab = Lab('Tn')
    lab.insert_tag('asfasf')
    lab.insert_tag('asfasf12314')
    print lab.tags