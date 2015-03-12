from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from datetime import datetime 
import unittest

base_url = "http://ldneqtsacs650dv.eur.nsroot.net:6543"
urls = {
    # Runs Menu list 
    "list_runs": r"/run_list_view",
    "run_detail": r"/runData_list_form/NAM",
    "run_regression": r"/runRegression_detail/NAM",
    "queue": r"/queue_detail",
    
    # Diffs Menu list
    "list_diffs": r"/diff_list_view",
    "generate_diff": r"/diff_generate_form/NAM",
    "summary_diffs": r"/diff_summary_form/ALL",
    "diff_detail": r"/diffData_list_form/ALL",
}

class TestMajestic(unittest.TestCase):
    
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)
    
    def tearDown(self):
        import time
        time.sleep(3)
        self.browser.close()
        
    def test_list_runs(self):
        browser = self.browser
        browser.get(go_page("list_runs"))
        
        
        paginate = self.wait.until(EC.element_to_be_clickable((By.XPATH, r"//*[@id='list_table_paginate']/span")))
        last_page = paginate.find_elements_by_class_name("paginate_button")[-1]
        last_page.click()
        
        table = browser.find_element_by_tag_name("tbody")
        last_row = browser.find_elements_by_tag_name("tr")[-1]

    def test_run_details(self):
        browser = self.browser
        browser.get(go_page("run_detail"))
        
        run_select = Select(browser.find_element_by_id("deformField1"))
        run_select.select_by_value("26")
        
        browser.find_element_by_id("deformsubmit").click()
        
    def test_queue(self):
        pass
        
    def test_run_regress(self):
        self._run_regress(r"NAM_Rth_22401_Green", r"UMI_2.21.0")

    def _run_regress(self, tag, build, model="vanilla"):
        browser = self.browser
        
        
        # wait = WebDriverWait(browser, 10)
        # menu = wait.until(EC.element_to_be_clickable((By.XPATH,r"/html/body/core-scaffold/core-header-panel/core-menu/core-submenu[1]/core-item[3]/a")))
        # menu.click()
        # browser.switch_to_frame(browser.find_element_by_tag_name("iframe"))
        
        browser.get(go_page("run_regression"))
        
        model_select = Select(browser.find_element_by_id("deformField2"))
        model_select.select_by_value(model)
        
        browser.find_element_by_id("deformField3").send_keys(tag)
        
        build_select = Select(browser.find_element_by_id("deformField4"))
        build_select.select_by_value(build)
        
        browser.find_element_by_id("deformField5").send_keys("QA_Test {0}".format(get_timestamp()))
        
        #browser.find_element_by_id("deformsubmit").click()
        
        #title = wait.until(EC.element_to_be_clickable((By.XPATH,r"/html/body/div[2]")))
        #self.assertEqual(title, "Submited Regression Test")

    def test_run_diff(self):
        self._run_diff("39", "366")
        
    def test_list_diffs(self):
        browser = self.browser
        browser.get(go_page("list_diffs"))
        
    def test_diff_detail(self):
        browser = self.browser
        browser.get(go_page("diff_detail"))
        
        diff_select = Select(browser.find_element_by_id("deformField1"))
        diff_select.select_by_value("495")
        
    def test_summary_diff(self):
        pass 
        
    def _run_diff(self, base_build, cand_build):
        browser = self.browser
        browser.get(go_page("generate_diff"))
        
        
        # wait = WebDriverWait(browser, 10)
        # menu = wait.until(EC.element_to_be_selected((By.XPATH,r"/html/body/core-scaffold/core-header-panel/core-menu/core-submenu[2]")))
        # import time 
        # time.sleep(10)
        # menu = browser.find_element_by_xpath(r"/html/body/core-scaffold/core-header-panel/core-menu/core-submenu[2]")
        # menu.click()
        # sub_menu = wait.until(EC.element_to_be_clickable((By.XPATH,r"/html/body/core-scaffold/core-header-panel/core-menu/core-submenu[2]/core-item[2]/a")))
        # sub_menu.click()
        
        # browser.switch_to_frame(browser.find_element_by_tag_name("iframe"))
        
        
        base = Select(browser.find_element_by_id("deformField1"))
        cand = Select(browser.find_element_by_id("deformField2"))
        # base_build = get_build(base.options, base_build) 
        # cand_build = get_build(cand.options, base_build)
        try:
            base.select_by_value(base_build)
            cand.select_by_value(cand_build)
        except:
            raise Exception("wrong build name")
        
        browser.find_element_by_id("deformsubmit").click()
        

def get_build(builds, text):
    
    for build in builds:
        if build.text.find(text)>0:
            print build.text
            return build.text
    return False 
    
def get_timestamp():
    now = datetime.now()
    return "{0}-{1}-{2} {3}:{4}".format(now.year, now.month, now.day, now.hour, now.minute)

def go_page(target, region="NAM"):
    url = base_url + urls[target]
    if url.find("NAM")>0:
        url = url.replace("NAM", region)
    return url
        
if __name__ == '__main__':
    unittest.main()
