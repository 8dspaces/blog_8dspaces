## Python里的结构（闭包，装饰器等...）


最近在看webpy框架的源码，同时也开始研究一些设计模式，感觉自己差的很远，所幸还在努力，把学习中的一些所思所想记录下来以备参考。   

在webpy这样大的项目中究竟该如何更好的组织代码呢，发现里面用到了很多函数内套函数的方式，最终的结果就是隐藏了实现的细节，给使用者提供更友好的接口， 而函数套函数就是闭包和装饰器，是函数式编程中的一种重要语法结构，被Python项目中大量使用。

主要参考了我喜欢的一个博主Vamei的文章  

+ [闭包](http://www.cnblogs.com/vamei/archive/2012/12/15/2772451.html)
+ [装饰器](http://www.cnblogs.com/vamei/archive/2013/02/16/2820212.html)


### 闭包（closure）

> **闭包(closure)** 是函数式编程的重要的语法结构。函数式编程是一种编程范式 (而面向过程编程和面向对象编程也都是编程范式)。在面向过程编程中，我们见到过函数(function)；在面向对象编程中，我们见过对象(object)。  **`函数和对象的根本目的是以某种逻辑方式组织代码，并提高代码的可重复使用性(reusability)。 `**  
**闭包也是一种组织代码的结构，它同样提高了代码的可重复使用性**。

>不同的语言实现闭包的方式不同。Python以函数对象为基础，为闭包这一语法结构提供支持的 (我们在特殊方法与多范式中，已经多次看到Python使用对象来实现一些特殊的语法)。Python一切皆对象，函数这一语法结构也是一个对象。在函数对象中，我们像使用一个普通对象一样使用函数对象，比如更改函数对象的名字，或者将函数对象作为参数进行传递。


一个函数和它的环境变量合在一起，就构成了一个闭包(closure)  
在Python中，所谓的闭包是一个包含有环境变量取值的函数对象。环境变量取值被保存在函数对象的__closure__属性中。比如下面的代码：

	def line_conf():
	    b = 15
	    def line(x):
	        return 2*x+b
	    return line       # return a function object
	
	b = 5
	my_line = line_conf()
	print(my_line.__closure__)
	print(my_line.__closure__[0].cell_contents)
	# __closure__里包含了一个元组(tuple)。这个元组中的每个元素是cell类型的对象。
	# 我们看到第一个cell包含的就是整数15，也就是我们创建闭包时的环境变量b的取值。

上面的例子意义不大，只是一个闭包基本的例子，而强大之处在于可以传参，因为内层函数可以使用到外层函数的环境变量
也就是__closure__, 成为一个更加强大的工具	
一个闭包的实际点的例子

	def line_conf(a, b):
	    def line(x):
	        return ax + b
	    return line
	
	line1 = line_conf(1, 1)
	line2 = line_conf(4, 5)
	print(line1(5), line2(5))

	# line1, line2 提供给使用者，避免了定义若干函数
	# 可以理解为一个函数生成器

闭包**有效的减少了函数所需定义的参数数目**。

>   这对于**并行运算**来说有重要的意义。在并行运算的环境下，我们可以让每台电脑负责一个函数，然后将一台电脑的输出和下一台电脑的输入串联起来。最终，我们像流水线一>   >   样工作，从串联的电脑集群一端输入数据，从另一端输出数据。这样的情境最适合只有一个参数输入的函数。闭包就可以实现这一目的。
 

函数闭包提供了函数对象一个运行环境。这时的**函数对象得以和上下文环境一起传递**，函数也就具有了状态，不同的状态可以导致函数拥有不同的行为

	def with_cnt(funcobj):
	    cnt = [0]
	    def wrapper(*args, **kwargs):
	        cnt[0] += 1
	        print cnt[0]
	        return funcobj(*args, **kwargs)
	    return cnt


### 装饰器（decorator） 

>**装饰器(decorator)**是一种高级Python语法。装饰器可以**对一个函数、方法或者类进行加工**。在Python中，我们有多种方法对函数和类进行加工，比如在Python闭包中，我们见到函数对象作为某一个函数的返回结果。相对于其它方式，装饰器语法简单，代码可读性高。因此，装饰器在Python项目中有广泛的应用。

装饰器是以一个callable对象为参数（可以是函数，方法这些实现了__call__方法的对象）进行加工，python 2.6之后更进一步可以用来加工类  
加工的结果是为类，方法加上一些额外的功能，而这种加工可以叠加使用，简单而强大

#### 基本体
    
    # 一个最基本装饰器的结构，针对方法
	def print_args(function):
        def wrapper(*args, **kwargs):
            print 'Arguments:', args, kwargs
            return function(*args, **kwargs)
        return wrapper
    
	@print_args
	def write(text):
	    print text
	
	# @print_args 这样的方式等价于:  
	# write = print_args(write)
	# write('foo')
	# 标准库中 @property 就是一种常用装饰器
	
	write('foo')
	
	# ---output ---
	Arguments: ('foo',) {}
	foo


#### 传参体  

而装饰器也可以含参数，传递参数给函数 
这里用了两层来对函数进行加工，实质是在装饰器外用了闭包，因为闭包可以记录它的环境变量，外层参数的传递可以被用在函数体内

	# a new wrapper layer
	def pre_str(pre=''):
	    # old decorator
	    def decorator(F):
	        def new_F(a, b):
	            print(pre + "input", a, b)
	            return F(a, b)
	        return new_F
	    return decorator
	
	# get square sum
	@pre_str('^_^')
	def square_sum(a, b):
	    return a**2 + b**2
	
	# get square diff
	@pre_str('T_T')
	def square_diff(a, b):
	    return a**2 - b**2
	
	print(square_sum(3, 4))
	print(square_diff(3, 4))

	# 等价的写法 square_sum = pre_str('^_^') (square_sum)
	# pre_str('^_^')返回的是函数


#### 装饰类体  
以一个类为参数，并在函数体内对类做相应的修改  

	def decorator(aClass):
	    class newClass:
	        def __init__(self, age):
	            self.total_display   = 0
	            self.wrapped         = aClass(age)

	        def display(self):
	            self.total_display += 1
	            print("total display", self.total_display)
	            self.wrapped.display()

	    return newClass
	
	@decorator
	class Bird:
	    def __init__(self, age):
	        self.age = age
	    def display(self):
	        print("My age is",self.age)
	
	eagleLord = Bird(5)
	for i in range(3):
	    eagleLord.display()


列一个webpy中用装饰器的方法，记录timeout,用到了传参体 

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


### 总结  
----
闭包和装饰器都是通过函数来实现的，可见python中函数的强大。一切皆对象，包括函数，方法，所有....
Python中函数和类之间可以相互包含的这种组织方式为结构的合理规划提供了很好的方式。 


+ 闭包： 一个函数和他的环境变量（）合在一起  -->被另一个函数包含  -->可以理解为一个函数生成器
+ 装饰器： 以函数，类为参数的一个加工函数（可能会用到多层），闭包是基础


更多参考：

[Vamei的博客](http://www.cnblogs.com/vamei/tag/Python/)
[动态生成（函数）对象](http://www.afewords.com/blog/5066b96437251776c4000006)