##WSGI 在webpy中的理解  
http://blog.tomsheep.net/2012/08/01/notes/ 


一个WSGI app就是一个具有以下签名的callable: 

  	def application(environ, start_response) 

environ是环境变量、http头、wsgi变量等的集合，start_response是用来处理status和headers的回调，这个接口设计的其实没有必要，wsgi2.0会去掉。这个application的返回值是一个iterable，是返回的http body内容。另外，start_response的签名是

      start_response(status, response_headers, exc_info=None)

这几乎就是wsgi最核心的内容了，wsgi是server和app之间的约定，只要web framework支持这样的调用方式，这样的framework就可以被实现了wsgi调用的web server支持。而web server如何实现对wsgi的支持呢？一般来讲，可以直接支持，很多python实现的web server就是；可以通过现有web server embed的方式支持，如mod_wsgi； 可以通过scgi或fcgi容器实现，如flup，因为scgi和fcgi都是web server普遍支持的和外部程序交互的接口，flup向下实现了scgi和fcgi的交互方式，向上实现了wsgi application的调用方式。

关于wsgi、scgi、fcgi、web server之间的关系，我觉得 这篇文章 是讲的比较清楚的一篇。

web.py code review：

web.py是一个轻量级的python web框架，代码不到10000 LOC， 其中包括了一个轻量http server

application.py: application类是程序主体，保存url mapping和环境参数。processor的概念相当于middleware，用一个列表储存所有注册的processor（通过app.add_processor注册），每个processor有这样的签名：

  	def processor(handle)

其中handle相当于nodejs connect middleware中的next，通过

      def handle_with_processors(self): 
          def process(processors): 
              try: 
                  if processors: 
                      p, processors = processors[0], processors[1:] 
                      return p(lambda: process(processors)) 
                  else: 
                      return self.handle() 
                  …… 
这样的方式实现顺序执行，最后的self.handle()调用就是filter过后url匹配的逻辑。

app.wsgifunc()函数返回一个wsgi callable（之前说过），用以和支持wsgi的server集成。

当调用app.run(*middleware)时，实际是调用wsgi.runwsgi(self.wsgifunc(*middleware))： 其中的middleware是wsgi middleware，原理就是把wsgi包装一层返回一个新的wsgi callable，和web中熟悉的filter概念是一致的

web.py的wsgi模块中提供了三种run的模式，fcgi, scgi, 还有http server：其中http server是直接用了CherryPy中的web server实现。


##更多的参考:    

### WSGI初探

此文来自本人原JavaEye博客。[原文地址](http://linluxiang.iteye.com/blog/799163)

前言

本文不涉及WSGI的具体协议的介绍，也不会有协议完整的实现，甚至描述中还会掺杂着本人自己对于WSGI的见解。所有的WSGI官方定义请看http://www.python.org/dev/peps/pep-3333/。

###WSGI是什么？

WSGI的官方定义是，the Python Web Server Gateway Interface。从名字就可以看出来，这东西是一个Gateway，也就是网关。网关的作用就是在协议之间进行转换。

也就是说，WSGI就像是一座桥梁，一边连着web服务器，另一边连着用户的应用。但是呢，这个桥的功能很弱，有时候还需要别的桥来帮忙才能进行处理。

下面对本文出现的一些名词做定义。wsgi app，又称应用 ，就是一个WSGI application。wsgi container ，又称容器 ，虽然这个部分常常被称为handler，不过我个人认为handler容易和app混淆，所以我称之为容器。 wsgi_middleware ，又称*中间件*。一种特殊类型的程序，专门负责在容器和应用之间干坏事的。

一图胜千言，直接来一个我自己理解的WSGI架构图吧

![](.\jpg\wsgi.jpg)

可以看出，服务器，容器和应用之间存在着十分纠结的关系。下面就要把这些纠结的关系理清楚。

###WSGI应用

WSGI应用其实就是一个callable的对象。举一个最简单的例子，假设存在如下的一个应用：

def application(environ, start_response):
  status = '200 OK'
  output = 'World!'
  response_headers = [('Content-type', 'text/plain'),
                      ('Content-Length', str(12)]
  write = start_response(status, response_headers)
  write('Hello ')
  return [output]
这个WSGI应用简单的可以用简陋来形容，但是他的确是一个功能完整的WSGI应用。只不过给人留下了太多的疑点，environ是什么？start_response是什么？为什么可以同时用write和return来返回内容？

对于这些疑问，不妨自己猜测一下他的作用。联想到CGI，那么environ可能就是一系列的环境变量，用来表示HTTP请求的信息，比如说method之类的。start_response，可能是接受HTTP response头信息，然后返回一个write函数，这个write函数可以把HTTP response的body返回给客户端。return自然是将HTTP response的body信息返回。不过这里的write和函数返回有什么区别？会不会是其实外围默认调用write对应用返回值进行处理？而且为什么应用的返回值是一个列表呢？说明肯定存在一个对应用执行结果的迭代输出过程。难道说他隐含的支持iterator或者generator吗？

等等，应用执行结果？一个应用既然是一个函数，说明肯定有一个对象去执行它，并且可以猜到，这个对象把environ和start_response传给应用，将应用的返回结果输出给客户端。那么这个对象是什么呢？自然就是WSGI容器了。

## WSGI容器

先说说WSGI容器的来源，其实这是我自己编造出来的一个概念。来源就是JavaServlet容器。我个人理解两者有相似的地方，就顺手拿过来用了。

WSGI容器的作用，就是构建一个让WSGI应用成功执行的环境。成功执行，意味着需要传入正确的参数，以及正确处理返回的结果，还得把结果返回给客户端。

所以，WSGI容器的工作流程大致就是，用webserver规定的通信方式，能从webserver获得正确的request信息，封装好，传给WSGI应用执行，正确的返回response。

一般来说，WSGI容器必须依附于现有的webserver的技术才能实现，比如说CGI，FastCGI，或者是embed的模式。

下面利用CGI的方式编写一个最简单的WSGI容器。关于WSGI容器的协议官方文档并没有具体的说如何实现，只是介绍了一些需要约束的东西。具体内容看PEP3333中的协议。

	#!/usr/bin/python
	#encoding:utf8  
	
	import cgi
	import cgitb
	import sys
	import os  
	
	#Make the environ argument
	environ = {}
	environ['REQUEST_METHOD'] = os.environ['REQUEST_METHOD']
	environ['SCRIPT_NAME'] = os.environ['SCRIPT_NAME']
	environ['PATH_INFO'] = os.environ['PATH_INFO']
	environ['QUERY_STRING'] = os.environ['QUERY_STRING']
	environ['CONTENT_TYPE'] = os.environ['CONTENT_TYPE']
	environ['CONTENT_LENGTH'] = os.environ['CONTENT_LENGTH']
	environ['SERVER_NAME'] = os.environ['SERVER_NAME']
	environ['SERVER_PORT'] = os.environ['SERVER_PORT']
	environ['SERVER_PROTOCOL'] = os.environ['SERVER_PROTOCOL']
	environ['wsgi.version'] = (1, 0)
	environ['wsgi.url_scheme'] = 'http'
	environ['wsgi.input']        = sys.stdin
	environ['wsgi.errors']       = sys.stderr
	environ['wsgi.multithread']  = False
	environ['wsgi.multiprocess'] = True
	environ['wsgi.run_once']     = True  
	
	#make the start_response argument
	#注意，WSGI协议规定，如果没有body内容，是不能返回http response头信息的。
	sent_header = False
	res_status = None
	res_headers = None  
	
	def write(body):
	    global sent_header
	    if sent_header:
	        sys.stdout.write(body)
	    else:
	        print res_status
	        for k, v in res_headers:
	            print k + ': ' + v
	        print
	        sys.stdout.write(body)
	        sent_header = True  
	
	def start_response(status, response_headers):
	    global res_status
	    global res_headers
	    res_status = status
	    res_headers = response_headers
	    return write  
	
	#here is the application
	  def application(environ, start_response):
	    status = '200 OK'
	    output = 'World!'
	    response_headers = [('Content-type', 'text/plain'),
	                        ('Content-Length', str(12)]
	    write = start_response(status, response_headers)
	    write('Hello ')
	    return [output]  
	
	#here run the application
	result = application(environ, start_response)
	for value in result:
	    write(value)
看吧。其实实现一个WSGI容器也不难。

不过我从WSGI容器的设计中可以看出WSGI的应用设计上面存在着一个重大的问题就是：为什么要提供两种方式返回数据？明明只有一个write函数，却既可以在application里面调用，又可以在容器中传输应用的返回值来调用。如果说让我来设计的话，直接把start_response给去掉了。就用application(environ)这个接口。传一个方法，然后返回值就是status, response_headers和一个字符串的列表。实际传输的方法全部隐藏了。用户只需要从environ中读取数据处理就行了。。

可喜的是，搜了一下貌似web3的标准里面应用的设计和我的想法类似。希望web3协议能早日普及。

##Middleware中间件

中间件是一类特殊的程序，可以在容器和应用之间干一些坏事。。其实熟悉python的decorator的人就会发现，这和decoraotr没什么区别。

下面来实现一个route的简单middleware。

	class Router(object):
	    def __init__(self):
	        self.path_info = {}
	    def route(self, environ, start_response):
	        application = self.path_info[environ['PATH_INFO']]
	        return application(environ, start_response)
	    def __call__(self, path):
	        def wrapper(application):
	            self.path_info[path] = application
	        return wrapper

这就是一个很简单的路由功能的middleware。将上面那段wsgi容器的代码里面的应用修改成如下：

	router = Router()  
	
	#here is the application
	@router('/hello')
	def hello(environ, start_response):
	    status = '200 OK'
	    output = 'Hello'
	    response_headers = [('Content-type', 'text/plain'),
	                        ('Content-Length', str(len(output)))]
	    write = start_response(status, response_headers)
	    return [output]  
	
	@router('/world')
	def world(environ, start_response):
	    status = '200 OK'
	    output = 'World!'
	    response_headers = [('Content-type', 'text/plain'),
	                        ('Content-Length', str(len(output)))]
	    write = start_response(status, response_headers)
	    return [output]
	#here run the application
	result = router.route(environ, start_response)
	for value in result:
	    write(value)

这样，容器就会自动的根据访问的地址找到对应的app执行了。

####延伸


其实从另外一个角度去考虑。如果把application当作是一个运算单元。利用middleware调控IO和运算资源，那么利用WSGI组成一个分布式的系统。