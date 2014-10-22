 Python新手常犯错误
 ====
 
 ### 用一个可变的值作为默认值
 
 **Bad**：
 
     def foo(numbers=[]):
        numbers.append(9)
        print numbers
 这样会出现的情况是，多次调用函数，变量会被重复改变
 
> foo() # first time, like before   
> [9]  
> foo() # second time  
> [9, 9]  
> foo() # third time...  
> [9, 9, 9]  
> foo() # WHAT IS THIS BLACK MAGIC?!  
> [9, 9, 9, 9]  
        
 **Good：** 
 
    def foo(numbers=None):
        if numbers is None:
            numbers = []
        numbers.append(9)
        print numbers

### 作用域
    
    # 使用全局变量应该多加注意
    bar = 42
    def foo():
        print bar  # 42
        bar = 0    # 实际是新建了一个局部变量bar 
     print bar     # 42
     
这里提供两种解决方式
    
一就是使用global 关键字     

    >>> bar = 42
    ... def foo():
    ...     global bar
    ...     print bar
    ...     bar = 0
    ... 
    ... foo()
    42
    >>> bar
    0
    
第二个方法，也是更推荐使用的，`就是不要使用全局变量`。如果你想保存在代码里至始至终用到的值的时候，`把它定义为一个类的属性`。用这种方法的话就完全不需要用global了，当你要用这个值的时候，通过类的属性来访问就可以了：

    >>> class Baz(object):
    ...     bar = 42
    ... 
    ... def foo():
    ...     print Baz.bar  # global
    ...     bar = 0  # local
    ...     Baz.bar = 8  # global
    ...     print bar
    ... 
    ... foo()
    ... print Baz.bar
    42
    0
    8