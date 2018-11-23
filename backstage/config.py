#--*-- coding:utf-8 --*--

class Config(dict):
    def __init__(self):
        dict.__init__(self)

    def __getattr__(self, item):
        if item not in self:
            raise  KeyError('have no attr')
        return self[item]
    def __setattr__(self, key, value):
        self[key]=value


