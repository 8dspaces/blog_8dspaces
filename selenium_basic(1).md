<link rel="stylesheet" href="http://yandex.st/highlightjs/8.0/styles/default.min.css">
<script src="http://yandex.st/highlightjs/8.0/highlight.min.js"></script>
<script>hljs.tabReplace = ' ';hljs.initHighlightingOnLoad();</script>

Selenium Basic(1)--识别对象  
========

### 识别对象
自动化中识别定位对象是一切操作的基础，只有定位到对象，才能进一步取得对象的控制权，操作，测试

**Webdriver** 中定位对象的方法，常用的有如下几种`其实对应的是DOM操作`  

* id
* name
* class name
* link text
* partial link text
* tag name
* xpath
* css selector  


### 常用方法举例:

    #########百度输入框的定位方式##########

    #通过id方式定位
    browser.find_element_by_id("kw").send_keys("selenium")

    #通过name方式定位
    browser.find_element_by_name("wd").send_keys("selenium")

    #通通tag name方式定位
    browser.find_element_by_tag_name("input").send_keys("selenium")

    #通过class name 方式定位
    browser.find_element_by_class_name("s_ipt").send_keys("selenium")

    #通过CSS方式定位
    browser.find_element_by_css_selector("#kw").send_keys("selenium")

    #通过xphan方式定位
    browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
 
 
### 扩展
 
**`find_element_*`**  是为要寻找单独的模
webdriver 中也有对应的寻找一系列的元素的方法，就是**`find_elements_*`**  

使用方法和 `find_element_*` 一样，不同的是返回的是一个列表，可以使用列表相关的操作方式
`browser.find_elements_by_tag_name("input").pop(0).send_keys("selenium")`

### 总结
selenium 定位方式:  

* `find_element_by_*` 
* `find_elements_by_*`

 
