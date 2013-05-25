# A lovely dot dictionary allows dot notation to access dictionary entries
class DotDict(dict):

    def __init__(self, items={}, **kwargs):
        super(DotDict, self).__init__(**kwargs)
        for key, value in items.iteritems():
            self[key] = value

    def __getattr__(self, attr):
        return self.get(attr, None)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
