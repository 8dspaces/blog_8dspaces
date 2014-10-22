# Selenium Start

#### 导入selenium

	from selenium import webdriver 
	
	# Same as Chrome, IE
	brower = webdriver.Firefor()
	 

#### 基本功能

+  brower.get(url)                # use to open given url
+  browser.title
+  browser.maximize_window
+  browser.set_window_size(600, 480)
+  browser.find_element_by_id(#id).send_keys(str)
+  browser.find_element_by_id(#id).click()
+  browser.quit()
