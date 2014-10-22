python 正则表达式（re）基础
====

正则表达式是通过一定的模式去匹配查找某字符串、文本中符合模式的文本
基本的语法并不难， 难的是根据实际的需求去建立合适的高效的正则表达式，各种语言都有对正则表达式的支持，python对正则表达式的操作都在 **re** 模块中

正则表达式实质也是字符串，只是很多字符在正则表达式中有不同的含义
类似于windows中的通配符，* --所有字符  ？-- 一个字符，只是正则要强大的多的多

## 建立正则表达式

正则可以在很多表达式中直接传表达式字符串进去，但如果涉及到大量的匹配查找时最好先编译
**`re.compile(pattern, flags=0)`**

    import re 
    reg = r"book[0-9][0-9]\.txt"  #匹配形如 book23.txt, book 40.txt
    book_re = re.copile(reg)  # book_re可以被使用在下一步的匹配函数中
    



## 使用

基本上每一个正则方法都有两种方式使用，以search方法为例

+  `re.search(pattern, string, flags=0)`  #模块方法  
    return a corresponding MatchObject instance  
    pattern -- 一个未编译的正则字符串  
    
+   `search(string[, pos[, endpos]]) ` # RegexObject类方法  
    经过编译的字符串就是一个RegexObject
    
可以根据不同的需求选择不同的方法，以下的内容以模块方法为例


## 不同场合，各取所需

+ `re.search(pattern, string, flags=0)`  
   #查找合适的字符串, return **`MatchObject`** instance or **None**
   
+ `re.match(pattern, string, flags=0)`  
   #判断合适的字符串，return **`MatchObject`**  
   从字符串一开始就判断，适合用作判断字符串是否满足条件
    
  search是返回所有适合的结果，match只返回第一个适合的结果  
  详细的参考[Search Vs Match](http://docs.python.org/2/library/re.html#search-vs-match) 

------------ 

+ `re.findall(pattern, string, flags=0)` 
   #查找所有，返回**一个列表**
   Return all non-overlapping matches of pattern in string, as a list of strings 
   
+ `re.finditer(pattern, string, flags=0)`   
   Return an **iterator yielding** **MatchObject** instances over all non-overlapping matches for the RE pattern in string

------------ 
   
+ `re.split(pattern, string, maxsplit=0, flags=0)`  
   # split字符串成一个列表
------------ 
   
+ `re.sub(pattern, repl, string, count=0, flags=0)`
   # 替换字符串

    > Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. If the pattern isn’t found, string is returned unchanged. **repl can be a string or a function**; if it is a string, any backslash escapes in it are processed. That is, \n is converted to a single newline character, \r is converted to a carriage return, and so forth. Unknown escapes such as \j are left alone. Backreferences, such as \6, are replaced with the substring matched by group 6 in the pattern. For example:    

+ `re.subn(pattern, repl, string, count=0, flags=0)`  
  > Perform the same operation as sub(), but return a tuple (new_string, number_of_subs_made).
  
------------ 
  
+ `re.escape(string)`
  > Return string with all non-alphanumerics backslashed; this is useful if you want to match an arbitrary literal string that may have regular expression metacharacters in it.
+ `re.purge()  #Clear the regular expression cache`
   > Clear the regular expression cache.

##如何建立一个复杂的表达式--参考 

1. #####单个字符:

    + .          任意的一个字符
    + a|b        字符a或字符b
    + [afg]      a或者f或者g的一个字符        
    + [0-4]      0-4范围内的一个字符
    + [a-f]      a-f范围内的一个字符
    + [^m]       不是m的一个字符
    + \s         一个空白
    + \S         一个非空白
    + \d         [0-9]
    + \D         [^0-9]
    + \w         [0-9a-zA-Z]  #字符对应的字母，符号
    + \W         [^0-9a-zA-Z] #非字母对应的符号


2. ##### 重复  紧跟在单个字符之后，表示多个这样类似的字符
    
    +  `* `        重复 >=0 次
    +  `+`         重复 >=1 次
    +  `? `        重复 0或者1 次
    +  `{m} `      重复m次。比如说 a{4}相当于aaaa，再比如说[1-3]{2}相当于[1-3][1-3]
    +  `{m, n}`    重复m到n次。比如说a{2, 5}表示a重复2到5次。小于m次的重复，或者大于n次的重复都不符合条件。   

3. #### 位置

    + ^         字符串的起始位置
    + $         字符串的结尾位置

4. ####返回控制

    我们有可能对搜索的结果进行进一步精简信息。比如下面一个正则表达式：
    `output_(\d{4})` 括号内的内容是group, 是一个非常常用的方式，从所要查找内容中返回需要的内容

    + (…)  

    >Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group; the contents of a group can be retrieved after a match has been performed, and can be matched later in the string with the \number special sequence, described below. To match the literals '(' or ')', use \( or \), or enclose them inside a character class: [(] [)].

    + (?...)  

    >This is an extension notation (a '?' following a '(' is not meaningful otherwise). The first character after the '?' determines what the meaning and further syntax of the construct is. Extensions usually do not create a new group; (?P<name>...) is the only exception to this rule. Following are the currently supported extensions.

    + (?iLmsux)  

    >(One or more letters from the set 'i', 'L', 'm', 's', 'u', 'x'.) The group matches the empty string; the letters set the corresponding flags: re.I (ignore case), re.L (locale dependent), re.M (multi-line), re.S (dot matches all), re.U (Unicode dependent), and re.X (verbose), for the entire regular expression. (The flags are described in Module Contents.) This is useful if you wish to include the flags as part of the regular expression, instead of passing a flag argument to the re.compile() function.

    >Note that the (?x) flag changes how the expression is parsed. It should be used first in the expression string, or after one or more whitespace characters. If there are non-whitespace characters before the flag, the results are undefined.

    + (?:...)  

    >A non-capturing version of regular parentheses. Matches whatever regular expression is inside the parentheses, but the substring matched by the group cannot be retrieved after performing a match or referenced later in the pattern.

    + (?P<name>...)  

    >Similar to regular parentheses, but the substring matched by the group is accessible via the symbolic group name name. Group names must be valid Python identifiers, and each group name must be defined only once within a regular expression. A symbolic group is also a numbered group, just as if the group were not named.

    >Named groups can be referenced in three contexts. If the pattern is (?        P<quote>['"]).*?(?P=quote) (i.e. matching a string quoted with either single or double quotes):


    + (?P=name)
    > A backreference to a named group; it matches whatever text was matched by the earlier group named name.

    + (?#…)
    > A comment; the contents of the parentheses are simply ignored.

    + (?=…)
    >Matches if ... matches next, but doesn’t consume any of the string. This is called a lookahead assertion. For example, Isaac (?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.

    + (?….)

    > Matches if ... doesn’t match next. This is a negative lookahead assertion. For example, Isaac (?!Asimov) will match 'Isaac ' only if it’s not followed by 'Asimov'.

    + (?<=...)

    > Matches if the current position in the string is preceded by a match for ... that ends at the current position. This is called a positive lookbehind assertion. (?<=abc)def will find a match in abcdef, since the lookbehind will back up 3 characters and check if the contained pattern matches. The contained pattern must only match strings of some fixed length, meaning that abc or a|b are allowed, but a* and a{3,4} are not. Note that patterns which start with positive lookbehind assertions will not match at the beginning of the string being searched; you will most likely want to use the search() function rather than the match() function:  

    
        import re
        m = re.search('(?<=abc)def', 'abcdef')
        m.group(0)
        'def'
        This example looks for a word following a hyphen:

        m = re.search('(?<=-)\w+', 'spam-egg')
        m.group(0)
        'egg'
     
    
    + (?<!…)

     > Matches if the current position in the string is not preceded by a match for .... This is called a negative lookbehind assertion. Similar to positive lookbehind assertions, the contained pattern must only match strings of some fixed length. Patterns which start with negative lookbehind assertions may match at the beginning of the string being searched.

    + (?(id/name)yes-pattern|no-pattern)

     >  Will try to match with yes-pattern if the group with given id or name exists, and with no-pattern if it doesn’t. no-pattern is optional and can be omitted. For example, (<)?(\w+@\w+(?:\.\w+)+)(?(1)>) is a poor email matching pattern, which will match with '<user@host.com>' as well as 'user@host.com', but not with '<user@host.com'.

#### 参考

+ [Python 官方链接](http://docs.python.org/2/library/re.html) 
+ [一个很好的基础教程](http://www.cnblogs.com/vamei/archive/2012/08/31/2661870.html)