import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from robot.api.logger import info, debug, console
from robot.api.deco import keyword
from time import sleep

console("Thư viện đã được import thành công")

class cus_lib:
    ROBOT_LIBRARY_SCOPE = 'TEST'

    def __init__(self):
        self.driver = None
       # self.arg1 = arg1
        service = None
        chrome_options = Options()
        chrome_options.add_argument("--disable-dev-shm-usage")  # Khắc phục lỗi bộ nhớ thấp
        chrome_options.add_argument("--use-gl=desktop")            # Chạy mà không cần sandbox (trên Linux)
        #chrome_options.add_argument("--headless")              # Chế độ không giao diện (nếu cần)
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)        

#Truy cap website
    @keyword ("Get Url")
    def get_url(self,url):
        self.driver.get(url)


    @keyword("Refresh Url")
    def refresh_url(self):
        self.driver.refresh()
#Load Data
    @keyword ("Load JSON Data")
    def load_json_data(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

#Auto Login
    @keyword("Login")
    def login(self,username,password,xuser,xpass,xlogin):
        self.driver.find_element(By.XPATH,xuser).send_keys(username)
        self.driver.find_element(By.XPATH,xpass).send_keys(password)
        self.driver.find_element(By.XPATH,xlogin).click()

#Verify URL
    @keyword("Verify URL")
    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        if expected_url != actual_url:
            raise AssertionError (f"Expected URL is {expected_url}, Actual URL is {actual_url}")

#Verify text
    @keyword("Verify Text")
    def verify_text(self,xtext, expected_text):
        actual_text = self.driver.find_element(By.XPATH,xtext).text.strip()
        if actual_text != expected_text:
            raise AssertionError(f"Expected is {expected_text}, Actual is {actual_text}")

#Clear Session
    @keyword("Clear Session")
    def clear_session(self):
        """Xóa cookie để xóa session đăng nhập hiện tại."""
        self.driver.delete_all_cookies()

#Click
    @keyword("Click")
    def click_emlement(self,locator):
        self.driver.find_element(By.XPATH,locator).click()

#Verify element is Displayed
    @keyword("Verify Element")
    def verify_element(self,xelement):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xelement)))
            return element.is_displayed()  # Trả về True hoặc False
        except NoSuchElementException:
            return False  # Trả về False nếu không tìm thấy phần tử\]
        