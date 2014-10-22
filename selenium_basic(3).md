<link rel="stylesheet" href="http://yandex.st/highlightjs/8.0/styles/default.min.css">
<script src="http://yandex.st/highlightjs/8.0/highlight.min.js"></script>
<script>hljs.tabReplace = ' ';hljs.initHighlightingOnLoad();</script>


Selenium_Basic(3)--学会等待
=====

在运行测试用例时，等待控件加载完毕，等待上一个step结束然后运行下一步骤是非常常见的需求
用slenium 可以支持什么样的方式去实现呢？

### time.sleep(x)

最初级的当然可以用python 自带模块的sleep 方法
也可以通过循环判断，当不满足条件时，就等待


    time_out = 20
    while <item_not_ready> and <not timeout>:
        time.sleep(1)
        check_item_status

    next step 

### Explicit Waits（ExpectedCondition）

selenium 作为一个成熟的测试工具，这样的需求必然可以支持
selenium 可以设定一系列的等待条件`expected_conditions`
以及等待方法`WebDriverWait(driver, time).until(<condition>)`

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
    from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

    driver = webdriver.Firefox()
    driver.get("http://somedomain/url_that_delays_loading")
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
    finally:
        driver.quit()


selenium 可以支持的condition 列在下面, 基本可以满足测试的各种需求

+ title_is
+ title_contains
+ presence_of_element_located
+ visibility_of_element_located
+ visibility_of
+ presence_of_all_elements_located
+ text_to_be_present_in_element
+ text_to_be_present_in_element_value
+ frame_to_be_available_and_switch_to_it
+ invisibility_of_element_located
+ element_to_be_clickable - it is Displayed and Enabled.
+ staleness_of
+ element_to_be_selected
+ element_located_to_be_selected
+ element_selection_state_to_be
+ element_located_selection_state_to_be
+ alert_is_present

        
    
### Implicit Waits
对于响应比较慢的页面，我们希望每一步都之间都能等待较长的时间
但又不想每一步之前都要用上面的方法，这时候selenium提供的Implicit Waits就可以帮忙实现
`driver.implicitly_wait(10)`

    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.implicitly_wait(10) # seconds
    driver.get("http://somedomain/url_that_delays_loading")
    myDynamicElement = driver.find_element_by_id("myDynamicElement") 
    
    
#### 总结
+ `time.sleep(time)`
+ `WebDriverWait(driver, time).until(<condition>)`
+ `driver.implicitly_wait(time)`