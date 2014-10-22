<script src="http://yandex.st/highlightjs/7.3/highlight.min.js"></script>
<link rel="stylesheet" href="http://yandex.st/highlightjs/7.3/styles/github.min.css">
<script>
  hljs.initHighlightingOnLoad();
</script>

#Writing a class decorator in Python[转]  


Hi there, currently I’m working in a project which will be basically to provide a RESTful API to be consumed by a third party application.
In the development I’m writing it using django-piston.

So, today I came across a problem which was basically to make sure a request wouldn’t trigger any handler methods if it wasn’t authenticated.
Those who already had this problem knows that most times the solution is simply to add a sort of login_required() decorator on your methods. The problem is that every time you want this behaviour in a certain class method you have to decorate it.

To overcome this issue, today I wrote a class decorator which made my code look cleaner and tonight I decided to write about on how to write a class decorator hoping that his might be useful for someone s it was for me.

So, let’s start with the classic method decorator where you have to decorate every single method of your class. The code will look something like this:

    # file:  method_decorator.py

    def method_decorator(fn):
        "Example of a method decorator"
        def decorator(*args, **kwargs):
            print "\tInside the decorator"
            return fn(*args, **kwargs)

        return decorator

    class MyFirstClass(object):
        """
        This class has all its methods decorated
        """
        @method_decorator
        def first_method(self, *args, **kwargs):
            print "\t\tthis is a the MyFirstClass.first_method"

        @method_decorator
        def second_method(self, *args, **kwargs):
            print "\t\tthis is the MyFirstClass.second_method"

    if __name__ == "__main__":
        print "::: With decorated methods :::"
        x = MyFirstClass()
        x.first_method()
        x.second_method()
        
If you run this code you will get something like:

[apalma@insys tests] python method_decorator.py 
::: With decorated methods :::
	Inside the decorator
		this is a the MyFirstClass.first_method
	Inside the decorator
		this is the MyFirstClass.second_method
Obviously, following this approach you will have to go through all the available methods and decorate the ones you want to change its default behaviour.

The other solution its to write a class decorator, where you select which methods to decorate passing their names as the decorator arguments.

The following code will make this happen:

    # file:  class_decorator.py
    def method_decorator(fn):
        "Example of a method decorator"
        def decorator(*args, **kwargs):
            print "\tInside the decorator"
            return fn(*args, **kwargs)

        return decorator


    def class_decorator(*method_names):
        def class_rebuilder(cls):
            "The class decorator example"
            class NewClass(cls):
                "This is the overwritten class"
                def __getattribute__(self, attr_name):
                    obj = super(NewClass, self).__getattribute__(attr_name)
                    if hasattr(obj, '__call__') and attr_name in method_names:
                        return method_decorator(obj)
                    return obj

            return NewClass
        return class_rebuilder


    @class_decorator('first_method', 'second_method')
    class MySecondClass(object):
        """
        This class is decorated
        """
        def first_method(self, *args, **kwargs):
            print "\t\tthis is a the MySecondClass.first_method"

        def second_method(self, *args, **kwargs):
            print "\t\tthis is the MySecondClass.second_method"

    if __name__ == "__main__":
        print "::: With a decorated class :::"
        z = MySecondClass()
        z.first_method()
        z.second_method()
Run the code, and the result that comes out is the following:

    [apalma@insys tests] python class_decorator.py 
    ::: With a decorated class :::
    	Inside the decorator
    		this is a the MySecondClass.first_method
    	Inside the decorator
    		this is the MySecondClass.second_method
As you can see the output and the program flow when calling the class methods was similar in both situations.

