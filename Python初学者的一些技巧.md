给Python初学者的一些技巧
====

###交换变量

    x = 6
    y = 5

    x, y = y, x

    print x
    >>> 5
    print y
    >>> 6
    
###if 语句在行内

    print "Hello" if True else "World"
    >>> Hello

###连接

下面的最后一种方式在绑定两个不同类型的对象时显得很cool。

    nfc = ["Packers", "49ers"]
    afc = ["Ravens", "Patriots"]
    print nfc + afc
    >>> ['Packers', '49ers', 'Ravens', 'Patriots']

    print str(1) + " world"
    >>> 1 world

    print '1' + " world"
    >>> 1 world

    print 1, "world"
    >>> 1 world
    print nfc, 1
    >>> ['Packers', '49ers'] 1
**Note** 字符串连接一般不使用+ 因为字符串属于不可变对象，每次相加都是新建对象
可以使用string.format
    
    "{0}----{1}".format(var1, var2)
    #or 
    "%s %s" % (var1, var2)
    
###数字技巧

    #除后向下取整
    print 5.0//2
    >>> 2
    # 2的5次方
    print 2**5
    >> 32
    注意浮点数的除法

    print .3/.1
    >>> 2.9999999999999996
    print .3//.1
    >>> 2.0
    
###数值比较

这是我见过诸多语言中很少有的如此棒的简便法

    x = 2
    if 3 > x > 1:
       print x
    >>> 2
    if 1 < x > 0:
       print x
    >>> 2
    
###同时迭代两个列表

    nfc = ["Packers", "49ers"]
    afc = ["Ravens", "Patriots"]
    for teama, teamb in zip(nfc, afc):
         print teama + " vs. " + teamb
         
         
    >>> Packers vs. Ravens
    >>> 49ers vs. Patriots
    
###带索引的列表迭代

    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    for index, team in enumerate(teams):
        print index, team 

    >>> 0 Packers  
    >>> 1 49ers  
    >>> 2 Ravens  
    >>> 3 Patriots 
 
###列表推导式

已知一个列表，我们可以刷选出偶数列表方法：

    numbers = [1,2,3,4,5,6]
    even = []
    for number in numbers:
        if number%2 == 0:
            even.append(number)
            
转变成如下：

    numbers = [1,2,3,4,5,6]
    even = [number for number in numbers if number%2 == 0]


###字典推导

和列表推导类似，字典可以做同样的工作：

    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    print {key: value for value, key in enumerate(teams)}
    
    >>> {'49ers': 1, 'Ravens': 2, 'Patriots': 3, 'Packers': 0}

###初始化列表的值

    items = [0]*3
    print items
    >>> [0,0,0]
    
###列表转换为字符串

    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    print ", ".join(teams)
    >>> 'Packers, 49ers, Ravens, Patriots'

###从字典中获取元素

我承认try/except代码并不雅致，不过这里有一种简单方法，尝试在字典中查找key，如果没有找到对应的alue将用第二个参数设为其变量值。

    data = {'user': 1, 'name': 'Max', 'three': 4}
    try:
       is_admin = data['admin']
    except KeyError:
       is_admin = False
       
替换诚这样：(**data.get("key",[defaultvalue])**)

    data = {'user': 1, 'name': 'Max', 'three': 4}
    is_admin = data.get('admin', False)
    
###获取列表的子集

有时，你只需要列表中的部分元素，这里是一些获取列表子集的方法。

    x = [1,2,3,4,5,6]
    #前3个
    print x[:3]
    >>> [1,2,3]
    #中间4个
    print x[1:5]
    >>> [2,3,4,5]
    #最后3个
    print x[-3:]
    >>> [4,5,6]
    #奇数项
    print x[::2]
    >>> [1,3,5]
    #偶数项
    print x[1::2]
    >>> [2,4,6]
    60个字符解决FizzBuzz

前段时间Jeff Atwood 推广了一个简单的编程练习叫FizzBuzz，问题引用如下：

写一个程序，打印数字1到100，3的倍数打印“Fizz”来替换这个数，5的倍数打印“Buzz”，对于既是3的倍数又是5的倍数的数字打印“FizzBuzz”。

这里就是一个简短的，有意思的方法解决这个问题：

    for x in range(101):print"fizz"[x%3*4::]+"buzz"[x%5*4::]or x

###集合

除了python内置的数据类型外，在collection模块同样还包括一些特别的用例，在有些场合Counter非常实用。如果你参加过在这一年的Facebook HackerCup，你甚至也能找到他的实用之处。

    from collections import Counter
    print Counter("hello")
    >>> Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

 
###迭代工具 **itertools** 很牛

和collections库一样，还有一个库叫itertools，对某些问题真能高效地解决。其中一个用例是查找所有组合，他能告诉你在一个组中元素的所有不能的组合方式

    from itertools import combinations
    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    for game in combinations(teams, 2):
        print game
    >>> ('Packers', '49ers')
    >>> ('Packers', 'Ravens')
    >>> ('Packers', 'Patriots')
    >>> ('49ers', 'Ravens')
    >>> ('49ers', 'Patriots')
    >>> ('Ravens', 'Patriots')

###False == True

比起实用技术来说这是一个很有趣的事，在python中，True和False是全局变量，因此：

    False = True
    if False:
       print "Hello"
    else:
       print "World"
    >>> Hello

