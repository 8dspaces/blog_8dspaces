# this is one is from web.py source code 

class Storage(dict):
    """
    A Storage object is like a dictionary except `obj.foo` can be used
    in addition to `obj['foo']`.
    
        >>> o = storage(a=1)
        >>> o.a
        1
        >>> o['a']
        1
        >>> o.a = 2
        >>> o['a']
        2
        >>> del o.a
        >>> o.a
        Traceback (most recent call last):
            ...
        AttributeError: 'a'
    
    """
    def __getattr__(self, key): 
        try:
            return self[key]
        except KeyError, k:
            raise AttributeError, k
    
    def __setattr__(self, key, value): 
        self[key] = value
    
    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            raise AttributeError, k
    
    def __repr__(self):     
        return '<Storage ' + dict.__repr__(self) + '>'

storage = Storage

class easyaccessdict(dict):
    def __getattr__(self,name):
        if name in self:
            return self[name]
        n=easyaccessdict()
        super(easyaccessdict,self).__setitem__(name, n)
        return n
    def __getitem__(self,name):
        if name not in self:
            #n = easyaccessdict()
            super(easyaccessdict,self).__setitem__(name,easyaccessdict())
        return super(easyaccessdict,self).__getitem__(name)
    def __setattr__(self,name,value):
        super(easyaccessdict,self).__setitem__(name,value)

class easyaccessdict_2(dict):
    def __getattr__(self, name):
        return self[name]
    def __setattr__(self, name, value):
        super(easyaccessdict_2,self).__setitem__(name,value)
    def __missing__(self, name):
        super(easyaccessdict_2,self).__setitem__(name, easyaccessdict())
        return super().__getitem__(name)
        

if __name__ == "__main__":
    test = easyaccessdict( )
    test.b.c = "abc"
    test.b.d = 'bcd'
    test.b['e'] = 'm'
    print test.b['s']
    test.b['s'] = 'aaaa'
    print test.b['s']
    print test.b.e
    print test['a']['b']['c']