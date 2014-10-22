<link rel="stylesheet" href="http://yandex.st/highlightjs/8.0/styles/default.min.css">
<script src="http://yandex.st/highlightjs/8.0/highlight.min.js"></script>
<script>hljs.tabReplace = ' ';hljs.initHighlightingOnLoad();</script>


Selenium_Basic(2)--操作
===

识别控件之后下一步就是操作控件
selenium支持哪些操作呢

### send_keys (文本框操作）

    `element.send_keys("some text")`

可以同时支持其他按键

    `element.send_keys(" and some", Keys.ARROW_DOWN)`

也可以清除文本框中内容
    `element.clear()`

### 表单操作


    element = driver.find_element_by_xpath("//select[@name='name']")
    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
        print "Value is: %s" % option.get_attribute("value")
        option.click()

上面的操作是要去的option中所有的选项，并选择，用循环实现
selenium 有更有效率的方式，那就是试用 Select类
    
    from selenium.webdriver.support.ui import Select
    
    select = Select(driver.find_element_by_xpath("xpath"))
    all_selected_options = select.all_selected_options
    To get all available options:

    options = select.options
    
    
也可以用于其他的控件 

    select = Select(driver.find_element_by_name(‘name’)) 
    select.select_by_index(index) 
    select.select_by_visible_text(“text”) 
    select.select_by_value(value)
    
    
取消选择

    select = Select(driver.find_element_by_id('id'))
    select.deselect_all()
    
提交表单
    
    # Assume the button has the ID "submit" :)
    driver.find_element_by_id("submit").click()
    
selenium有更方便的方式提交表单
    
    # call within a form, elese will get Exception
    element.submit()
    
### Drag and Drop(拖拽)
    
    element = driver.find_element_by_name("source")
    target = driver.find_element_by_name("target")

    from selenium.webdriver import ActionChains
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(element, target)
    
### 多窗口，frames 之间移动

    <a href="somewhere.html" target="windowName">Click here to open a new window</a> 
    
    driver.switch_to_window("windowName")  # get window name from the above code

    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    
frame 之间移动

    `driver.switch_to_frame("frameName")`
    
It’s possible to access subframes by separating the path with a dot, and you can specify the frame by its index too. That is:

    `driver.switch_to_frame("frameName.0.child")`
    
would go to the frame named “child” of the first subframe of the frame called “frameName”. All frames are evaluated as if from *top*.

Once we are done with working on frames, we will have to come back to the parent frame which can be done using:

    `driver.switch_to_default_content()`

### 弹出窗口

    alert = driver.switch_to_alert() 
    
### 前进，后退

    driver.get("http://www.example.com")
    # To move backwards and forwards in your browser’s history:

    driver.back()
    driver.forward()
    
### Cookies
Before we leave these next steps, you may be interested in understanding how to use cookies. 
First of all, you need to be on the domain that the cookie will be valid for:

    # Go to the correct domain
    driver.get("http://www.example.com")

    # Now set the cookie. This one's valid for the entire domain
    cookie = {"key": "value"})
    driver.add_cookie(cookie)

    # And now output all the available cookies for the current URL
    all_cookies = **driver.get_cookies()**
    for cookie_name, cookie_value in all_cookies.items():
        print "%s -> %s", cookie_name, cookie_value

