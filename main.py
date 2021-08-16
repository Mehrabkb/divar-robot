from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Divar:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'https://divar.ir/s/tehran'
        self.ads_links = []
        self.driver.get(self.base_url)
        print('divar loading successful ...') 
        # self.login()
        self.home_search()

    def login(self):
        print('login starting')
        driver = self.driver
        my_posts_tag = driver.find_element_by_css_selector('a[href="/my-divar/my-posts"]')
        my_posts_tag.click()
        sleep(6)
        btn_login_init = driver.find_element_by_css_selector('button[class*="login-message__login-btn"]')
        btn_login_init.click()
        sleep(6)
        input_mobile = driver.find_element_by_css_selector('input[name="mobile"]')
        input_mobile.clear()
        input_mobile.send_keys("09369849997")
        input_mobile.send_keys(Keys.RETURN)
        sleep(30)
        print('login finish')
        self.home_search()

    def home_search(self):
        print('start work')
        driver = self.driver
        driver.get(self.base_url)
        driver.execute_script('document.getElementsByClassName("search-bar-box__placeholder")[0].innerHTML = null');
        input_search = driver.find_element_by_id('react-select-search-bar-input')
        input_search.clear()
        input_search.send_keys("طراحی سایت")
        input_search.send_keys(Keys.RETURN)
        links = driver.find_elements_by_css_selector('div[class*="post-card-item"] a')
        for link in links:
            print(link.get_attribute('href'))
        # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        for i in range(20):
            sleep(50)
            page = driver.find_element_by_tag_name('html')
            page.send_keys(Keys.END)
            links = driver.find_elements_by_css_selector('div[class*="post-card-item"] a')
            for link in links:
                print(link.get_attribute('href'))
print('starting app ...')
d = Divar()

