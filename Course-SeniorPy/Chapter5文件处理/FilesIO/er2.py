class CustomError(Exception):
    def __init__(self, info):
        Exception.__init__(self)
        self.errorinfo = info

    def __str__(self):
        return 'CustionError:%s' % self.errorinfo

try:
    raise CustomError('test CustomError')
except CustomError as e:
    print 'ErrorInfo:%s' % e
