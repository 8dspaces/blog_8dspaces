<script src="http://yandex.st/highlightjs/7.3/highlight.min.js"></script>
<link rel="stylesheet" href="http://yandex.st/highlightjs/7.3/styles/github.min.css">
<script>
  hljs.initHighlightingOnLoad();
</script>

#清晰理解wsgi


wsgi是一套**规范**，用来标准化Web Server和Web framework/app之间的接口。它不是server不是framework也不是middleware，只是`一套用来标准化接口的规范`。

由于目前主流的Python Web frameworks都支持wsgi, 因此一般情况下只需要知道如何配置就可以了，无需了解它的具体细节。

##一些总结

这套规范将web组件分为三部分：`server`, `framework/app`, `middleware`对象。

## Web server side

Server 必须提供两样东西：

  + `environ` 

    environ 是一个python dictionary，包含一些常见的东西(和CGI environment类似)。
    
  + `start_response` 函数。

    `start_response` 是一个callable对象，有两个参数: 
     + `status` —— string类型,包含一个标准的HTTP status 像"200 OK",
     + `response_headers` —— list类型,包含标准HTTP response headers。

## Web framework/app side

`对server而言，framework/app 就是一个callable`, 可以是class, object, function。用到的参数就是上面提到的`environ`和`start_response`。`返回一个iterable对象`。

## Middleware

中间件，顾名思义在Web server和Web framework/app之间再插入一个环节。看情况对数据做一些处理。

一个简单的例子

假设你运行一个服务器程序，自带的或第三方的。从Server Side来看，就是

    serve(myapp)
    
它会传递environ和start_response给myapp
从Framework/app Side来看，

    def myapp(environ, start_response):
        status = '200 OK'
        response_headers = [('Content-type','text/plain')]
        start_response(status, response_headers)
        return ['Hello World!\n']
        
它接收参数，并返回了一个list。
这就是一个简单的WSGI application了。
如果添加一个中间件,用来完成将字母转换为大写的功能，如下

    class Upperware:
        def __init__(self,app):
            self.wrapper = app
        def __call__(self, environ, start_response):
            for data in self.wrapper(environ, start_response):
                return data.upper()
                
那么Server Side来看，就是

    wrapper = Upperware(myapp)
    serve(wrapper)
    
    # wrapper成功的插了一脚先：）