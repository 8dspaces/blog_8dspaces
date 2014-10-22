<script src="http://yandex.st/highlightjs/7.3/highlight.min.js"></script>
<link rel="stylesheet" href="http://yandex.st/highlightjs/7.3/styles/github.min.css">
<script>
  hljs.initHighlightingOnLoad();
</script>

# Python碎碎念(一)


1. `类装饰器`在python2.6 之后被引用，其原理和函数，方法的装饰器类似
以类为参数，可以针对类本身做修改，或针对构造类做修改以影响创建的对象（instance），或和方法装饰器一样，只是针对某个方法做修改

>Python 2.6 and 3.0 extend decorators to work on classes too. As described earlier, while similar in concept to function decorators, class decorators are applied to classes instead—they may be used either to 

>   + manage classes themselves
   + or to intercept instance creation calls in order to manage instances. 
   + Also like function decorators

>class decorators are really just optional syntactic sugar, though many believe that they make a programmer’s intent more obvious and minimize erroneous calls.

    instances = {}
    def getInstance(aClass, *args):                 # Manage global table
        if aClass not in instances:                 # Add **kargs for keywords
            instances[aClass] = aClass(*args)       # One dict entry per class
        return instances[aClass]

    def singleton(aClass):                          # On @ decoration
        def onCall(*args):                          # On instance creation
            return getInstance(aClass, *args)
        return onCall
To use this, decorate the classes for which you want to enforce a single-instance model:

    @singleton                                      # Person = singleton(Person)
    class Person:                                   # Rebinds Person to onCall
         def __init__(self, name, hours, rate):     # onCall remembers Person
            self.name = name
            self.hours = hours
            self.rate = rate
         def pay(self):
            return self.hours * self.rate

    @singleton                                      # Spam = singleton(Spam)
    class Spam:                                     # Rebinds Spam to onCall
        def __init__(self, val):                    # onCall remembers Spam
            self.attr = val

    bob = Person('Bob', 40, 10)                     # Really calls onCall
    print(bob.name, bob.pay())

    sue = Person('Sue', 50, 20)                     # Same, single object
    print(sue.name, sue.pay())

    X = Spam(42)                                    # One Person, one Spam
    Y = Spam(99)
    print(X.attr, Y.attr)
    
    

Now, when the Person or Spam class is later used to create an instance, the wrapping logic layer provided by the decorator routes instance construction calls to onCall, which in turn calls getInstance to manage and share a single instance per class, regardless of how many construction calls are made. Here’s this code’s output:

    Bob 400
    Bob 400
    42 42

Interestingly, you can code a more self-contained solution here if you’re able to use the nonlocal statement (available in Python 3.0 and later) to change enclosing scope names, as described earlier—the following alternative achieves an identical effect, by using one enclosing scope per class, instead of one global table entry per class:

    def singleton(aClass):                          # On @ decoration
        instance = None
        def onCall(*args):                          # On instance creation
            nonlocal instance                       # 3.0 and later nonlocal
            if instance == None:
                instance = aClass(*args)            # One scope per class
            return instance
        return onCall
This version works the same, but it does not depend on names in the global scope outside the decorator. In either Python 2.6 or 3.0, you can also code a self-contained solution with a class instead—the following uses one instance per class, rather than an enclosing scope or global table, and works the same as the other two versions (in fact, it relies on the same coding pattern that we will later see is a common decorator class blunder; here we want just one instance, but that’s not always the case):

    class singleton:
        def __init__(self, aClass):                 # On @ decoration
            self.aClass = aClass
            self.instance = None
        def __call__(self, *args):                  # On instance creation
            if self.instance == None:
                self.instance = self.aClass(*args)  # One instance per class
            return self.instance
To make this decorator a fully general-purpose tool, store it in an importable module file, indent the self-test code under a __name__ check, and add support for keyword arguments in construction calls with **kargs syntax (I’ll leave this as a suggested exercise).