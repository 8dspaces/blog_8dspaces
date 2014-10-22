<script src="http://yandex.st/highlightjs/7.3/highlight.min.js"></script>
<link rel="stylesheet" href="http://yandex.st/highlightjs/7.3/styles/github.min.css">
<script>
  hljs.initHighlightingOnLoad();
</script>

# 一些术语的总结


+ ##Apache/lighttpd  

   相当于一个**request proxy**，根据配置，**把不同的请求转发给不同的server处理**，例如
  + **静态的文件**请求自己处理，这个时候它就像一个web server，
  + 对于fastcgi/python这样的请求, 转发给flup这样的**Server/Gateway**进行处理

    >Apache/Lighttpd:  HTTP Server(Web服务器),如同原文所说 HTTP Server其实相当于一个 request proxy(请求代理),它们负责解析 HTTP 协议，因为你不能在自己的程序中先 解析HTTP 协议，然后在进行响应的处理。这样的话 第一增加了程序员的工作难度(HTTP解析还真有点负责) 第二：程序会变的复杂，不易修改。所以我们就把解析HTTP协议这个工作交给一种专门的软件来做----HTTP Server。HTTP协议的解析的工作完成了，协议被解析成各种请求，那谁来处理这些请求来？当请求是一个静态文件(HTML文件)的时候，HTTP Server则会自己处理这些请求，此时HTTP Server 就相当于一个Web Server。但当我们请求的是一个 cgi/fastcgi/python 脚本的时候呢？很明显HTTP Server就处理不了啦，因为这些脚本无法直接转换为HTML文本，要依赖于某种特定的容器(环境)下才可以，对于 cgi/fastcgi/python 这样的请求转发给flup这样的Server/Gateway进行处理。就比如我们在Java Web中要请求一个Servlet时,普通的HTTP Server肯定处理不了，Servelt只能运行在实现了Servelt规范的服务器上才可以。

+ ##flup (one WSGI Server)

    一个用python写的web server，也就是cgi中所谓的Server/Gateway，它负责接受 `apache/lighttpd转发的请求`，并`调用你写的程序 (application)`，并将application处理的`结果返回到apache/lighttpd`

    + CherryPy：web server(and a web framework), webpy默认使用的
    + mod_wsgi：mod_wsgi是一个WSGI兼容的模块,能够在Apache HTTP Server 上运行 WSGI应用
    + Werkzeug: Flask使用的
    
    
+ ##CGI (Common Gateway Interface)  
    
    一种替代用户直接访问服务器上文件而诞生的“代理”， 用户通过CGI弧度动态数据和文件  
    CGI是一种为用户动态提供所需数据的设计思想，它有很多各种不同语言的实现
    
    web服务器负责接收http请求，但是http请求从request到response的过程需要有应用程序的逻辑处理，web服务器一般是使用C写的，比如nginx，apache。而应用程序则是由各种语言编写，比如php，java，python等。这两种语言要进行交互就需要有个协议进行规定，而cgi就是这么个网关协议。
    
+ ##fastCGI 

    apache/lighttpd的一个模块

    由于CGI每次创建进程销毁进程，效率不高，所以有了fastCGI的实现
    
    虽然flup可以作为一个独立的web server使用，但是`对于浏览器请求处理一般都交给 apache/lighttpd处理`，然后由apache/lighttpd`转发给flup处理`，这样就需要`一个东西来把apache/lighttpd跟flup联系起来`，这个东西就是**fastcgi**，它通过**环境变量以及socket**将客户端请求的信息传送给flup并接收flup返回的结果 -->做相关的配置


+ ##Web framework(web.py/django)

    有了上面的东西你就可以开始编写你的web程序了，但是问题是你就要自己处理浏览器的输入输出，还有cookie、session、模板等各种各样的问题了，web.py的作用就是帮你把这些工作都做好了，它就是所谓的web framework



+ ##WSGI（Web Server Gateway Interface）

    WSGI是Python对CGI进行的一种包装，核心使用Python实现，具体实现通常来说也需要使用Python    
    拿nginx+fastcgi+php为例子，nginx里面的fastcgi模块实现cgi的客户端，php的cgi-sapi实现cgi的服务端。

    WSGI就是Python的CGI包装，相对于Fastcgi是PHP的CGI包装

    除了flup Server/Gateway外还有很多其他人的写的Server/Gateway, 这个时候就会出问题了，如果你在flup上写了一个程序，现在由于各种原因你要使用xdly了，这个时候你的程序也许就要做很多痛苦的修改才能使用 xdly server了，WSGI就是一个规范，他规范了flup这个服务应该怎么写，应该使用什么方式什么参数调用你写的程序(application)等，当然同时也规范你的程序应该怎么写了，这样的话，只要flup跟xdly都遵守WSGI的话，你的程序在两个上面都可以使用了，flup就是一个 
             
    
        #一个典型WSGI应用的例子
        app = A_WSGI_Application(...)
        app = Middleware1(app, ...)
        app = Middleware2(app, ...)
        ...
        server(app).serve_forever()
        
        
##更多的参考：

+ [WSGI org document](http://wsgi.readthedocs.org/en/latest/)

+ ####一篇关于WSGI，CGI的回答列在这里： 
 
**How WSGI, CGI, and the frameworks are all connected ?**

`Apache` listens on port 80. It gets an HTTP request. It parses the request to find a way to respond. Apache has a LOT of choices for responding. 

+ One way to respond is to use CGI to run a script. 
+ Another way to respond is to simply serve a file.

In the case of `CGI`, Apache prepares an `environment and invokes the script` through the CGI protocol. This is a standard Linux Fork/Exec situation -- the CGI subprocess inherits an OS environment including the socket and stdout. The CGI subprocess writes a response, which goes back to Apache; Apache sends this response to the browser.

`CGI` is primitive and annoying. Mostly because it forks a subprocess for every request.

`WSGI` is an **interface** that is based on the CGI design pattern. It is not necessarily CGI -- it does not have to fork a subprocess for each request. It can be CGI, but it doesn't have to be.

WSGI adds to the CGI design pattern in several important ways. It parses the HTTP Request Headers for you and adds these to the environment. It supplies any POST-oriented input as a file-like object in the environment. It also provides you a function that will formulate the response, saving you from a lot of formatting details.

What do I need to know / install / do if I want to run a web framework (say web.py or cherrypy) on my basic CGI configuration ?

Recall that forking a subprocess is expensive. There are two ways to work around this.

+ Embedded `mod_wsgi` or `mod_python` embeds Python inside Apache; no process is forked. Apache runs the Django application directly.

+ Daemon `mod_wsgi` or `mod_fastcgi` allows Apache to interact with a separate daemon (or "long-running process"), using the WSGI protocol. You start your long-running Django process, then you configure Apache's mod_fastcgi to communicate with this process.

Note that mod_wsgi can work in either mode: embedded or daemon.

When you read up on `mod_fastcgi`, you'll see that `Django` uses `flup` to create a WSGI-compatible interface from the information provided by mod_fastcgi. The pipeline works like this.

`Apache -> mod_fastcgi -> FLUP (via CGI protocol) -> Django (via WSGI protocol)`

Django has several "django.core.handlers" for the various interfaces.

+ For `mod_fastcgi`, Django provides a manage.py runfcgi that integrates FLUP and the handler.

+ For `mod_wsgi,` there's a core handler for this.

How to install WSGI support ?

Follow these instructions.

[IntegrationWithDjango](http://code.google.com/p/modwsgi/wiki/IntegrationWithDjango)

For background see this

[Backgroud ](http://docs.djangoproject.com/en/dev/howto/)
    