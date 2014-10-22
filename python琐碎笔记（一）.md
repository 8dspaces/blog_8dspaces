<script src="http://yandex.st/highlightjs/7.3/highlight.min.js"></script>
<link rel="stylesheet" href="http://yandex.st/highlightjs/7.3/styles/github.min.css">
<script>
  hljs.initHighlightingOnLoad();
</script>

#Python琐碎笔记（一）


1.  对于一些不需要用到变量名的地方，纯计数，省去纠结i 还是j 
    `[[] for _ in range(10)]`
    
2.  列表slice 操作

        alist = [_ for _ in range(10)]
        a = alist[:]     # 复制
        b = alist[::-1]  # 反序，reverse
        c = alist[::2]   # 取偶数项目

        alist[0:] #列出0以后的
        alist[:-1] #列出-1之前的

        print a
        print b 
        print c 
        ========output===============
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        [0, 2, 4, 6, 8]
        
3. 用于判断一个对象的类型 isinstance
 
        #用于判断一个对象的类型， 代替if type(s) == type("") 之类的方法
        s = "abc"
        if isinstance(s, str):
            print "bingo"
        # 而isinstance第二个参数可以传tuple 
        isinstance(s, (str, list, tuple))
4. 让dict可以通过点操作符访问item (__getattr__)

        # 想让一个类拥有像字典一样的操作方式
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

        o = storage(a = 1)
        print o.a

        setattr(o, 'x', 3)
        print o.x 

5. `__getattr__` 和 `__getattribute__`区别

    >With objects, you need to deal with its attributes. Ordinarily we do instance.attribute

    >Some times we need more control (when we do not know the name of attribute in advance)

    >instance.attribute would become getattr(instance, attribute_name)

    >Using this model we can get the attribute by supplying the attribute_name. This works when we give a name as a string and you need to look up the instance attribute referenced by that name.

    >###Use of __getattr__

    >You can also tell a class how to deal with attributes it doesn’t explicitly manage and do that via __getattr__ method

    >Python will call it whenever you request an attribute that hasn’t already been defined. So you can define what to do with it.

    >###A classic usecase:

        class A(dict):
            def __getattr__(self, name):
               return self[name]
        a = A()
        # Now a.somekey will give a['somekey']
    
    >Caveats and use of __getattribute__

    >If you need to catch every attribute regardless whether it exists or not, use __getattribute__ instead.

    >###Difference

    >__getattr__ only gets called for attributes that don’t actually exist. If you set the attribute directly, referencing that attribute will retrieve it without calling __getattr__.

    >__getattribute__ is called all the times.


6. 任意数转36进制（来自webpy）

        def to36(q):
            """
            Converts an integer to base 36 (a useful scheme for human-sayable IDs).
            
                >>> to36(35)
                'z'
                >>> to36(119292)
                '2k1o'
                >>> int(to36(939387374), 36)
                939387374
                >>> to36(0)
                '0'
                >>> to36(-393)
                Traceback (most recent call last):
                    ... 
                ValueError: must supply a positive integer
            
            """
            if q < 0: raise ValueError, "must supply a positive integer"
            letters = "0123456789abcdefghijklmnopqrstuvwxyz"
            converted = []
            while q != 0:
                q, r = divmod(q, 36)
                converted.insert(0, letters[r])
            return "".join(converted) or '0'
            
7. timeout装饰器

        def timelimit(timeout):
        """
        A decorator to limit a function to `timeout` seconds, raising `TimeoutError`
        if it takes longer.
        
            >>> import time
            >>> def meaningoflife():
            ...     time.sleep(.2)
            ...     return 42
            >>> 
            >>> timelimit(.1)(meaningoflife)()
            Traceback (most recent call last):
                ...
            TimeoutError: took too long
            >>> timelimit(1)(meaningoflife)()
            42

        _Caveat:_ The function isn't stopped after `timeout` seconds but continues 
        executing in a separate thread. (There seems to be no way to kill a thread.)

        inspired by <http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/473878>
        """
        def _1(function):
            def _2(*args, **kw):
                class Dispatch(threading.Thread):
                    def __init__(self):
                        threading.Thread.__init__(self)
                        self.result = None
                        self.error = None

                        self.setDaemon(True)
                        self.start()

                    def run(self):
                        try:
                            self.result = function(*args, **kw)
                        except:
                            self.error = sys.exc_info()

                c = Dispatch()
                c.join(timeout)
                if c.isAlive():
                    raise TimeoutError, 'took too long'
                if c.error:
                    raise c.error[0], c.error[1]
                return c.result
            return _2
        return _1
        
8. 计数优化

        def commify(n):
        """
        Add commas to an integer `n`.

            >>> commify(1)
            '1'
            >>> commify(123)
            '123'
            >>> commify(1234)
            '1,234'
            >>> commify(1234567890)
            '1,234,567,890'
            >>> commify(123.0)
            '123.0'
            >>> commify(1234.5)
            '1,234.5'
            >>> commify(1234.56789)
            '1,234.56789'
            >>> commify('%.2f' % 1234.5)
            '1,234.50'
            >>> commify(None)
            >>>

        """
        if n is None: return None
        n = str(n)
        if '.' in n:
            dollars, cents = n.split('.')
        else:
            dollars, cents = n, None

        r = []
        for i, c in enumerate(str(dollars)[::-1]):
            if i and (not (i % 3)):
                r.insert(0, ',')
            r.insert(0, c)
        out = ''.join(r)
        if cents:
            out += '.' + cents
        return out
        
9. 序列字符串

        def nthstr(n):
        """
        Formats an ordinal.
        Doesn't handle negative numbers.

            >>> nthstr(1)
            '1st'
            >>> nthstr(0)
            '0th'
            >>> [nthstr(x) for x in [2, 3, 4, 5, 10, 11, 12, 13, 14, 15]]
            ['2nd', '3rd', '4th', '5th', '10th', '11th', '12th', '13th', '14th', '15th']
            >>> [nthstr(x) for x in [91, 92, 93, 94, 99, 100, 101, 102]]
            ['91st', '92nd', '93rd', '94th', '99th', '100th', '101st', '102nd']
            >>> [nthstr(x) for x in [111, 112, 113, 114, 115]]
            ['111th', '112th', '113th', '114th', '115th']

        """
        
        assert n >= 0
        if n % 100 in [11, 12, 13]: return '%sth' % n
        return {1: '%sst', 2: '%snd', 3: '%srd'}.get(n % 10, '%sth') % n