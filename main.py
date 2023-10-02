from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class Republik:
    def __init__(self):
        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
    
    def login_facebook(self):
        self.driver.get("https://web.facebook.com/")
        time.sleep(2)
        email = self.driver.find_element(By.NAME, 'email')
        password = self.driver.find_element(By.NAME, 'pass')
        email.send_keys("61551934197850")  # Ganti dengan username Facebook yang valid
        password.send_keys("Visual2023@#")  # Ganti dengan password Facebook yang valid
        password.send_keys(Keys.ENTER)
        time.sleep(2)

        print('Berhasil Login Facebook')

    def login_republik(self):
        self.driver.get("https://app.republik.gg/auth/log-in-option")
        time.sleep(8)
        self.driver.find_element(By.CSS_SELECTOR, ".mt-4 > span").click()
        time.sleep(15)
        windows = self.driver.window_handles
        if len(windows) >= 10:
            self.driver.switch_to.window(windows[1])
            time.sleep(20)
            self.driver.find_element(By.CSS_SELECTOR, ".xtk6v10 > .x1lliihq").click()
            time.sleep(20)
            windows = self.driver.window_handles
            if len(windows) >= 10:
                self.driver.switch_to.window(windows[2])
                time.sleep(20)
                
        print('Berhasil Login Republik')

    def find_followers(self):
        self.driver.get("https://app.republik.gg/relations/b4dc1e11-a507-4d18-9dc4-8400f57b28a7?following=true")
        time.sleep(6)

        while True:
            time.sleep(3)
            buttons = self.driver.find_elements(By.CSS_SELECTOR, '.ion-content-scroll-host > div > div:nth-child(1) > div ion-button.font-bold')

            print("Follow Start")

            print(buttons)

            for button in buttons:
                button.click()
                print(button.text)
                time.sleep(0.3)

            #self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight")
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            scroll = self.driver.find_element(By.CLASS_NAME, 'input-wrapper')
            scroll.click()
            scroll.send_keys(Keys.SPACE)

            time.sleep(3)


            print("Follow End")

# Penggunaan:
republik = Republik()
republik.login_facebook()
republik.login_republik()
republik.find_followers()

