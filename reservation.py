import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Reservation:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # path = os.getcwd()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        # self.driver = webdriver.Chrome((path + "/chromedriver_linux"), options=chrome_options)
        self.driver.get('http://www.net.city.nagoya.jp/sporec/index.html')
        time.wait(3)
        print(self.driver.title)

    def check(self, input_month, input_day):
        # place_search = self.driver.find_element(By.XPATH, '//a[@href="https://www.net.city.nagoya.jp/cgi-bin/sp04001"]')
        place_search = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//a[@href="https://www.net.city.nagoya.jp/cgi-bin/sp04001"]')))
        place_search.click()

        # 種目の選択
        event = self.driver.find_element(By.NAME, 'syumoku')
        event_select = Select(event)
        event_select.select_by_value('024')

        # 利用日の選択
        month = self.driver.find_element(By.NAME, 'month')
        month_select = Select(month)
        month_select.select_by_value(input_month)

        day = self.driver.find_element(By.NAME, 'day')
        day_select = Select(day)
        day_select.select_by_value(input_day)

        # 希望条件の選択
        # radio_button = driver.find_element(By.XPATH, '//*[@id="main"]/table[2]/tbody/tr[2]/td[4]/input[2]')
        # radio_button.click()

        # 供用区分の選択
        usage = self.driver.find_element(By.NAME, 'kyoyo1')
        usage_select = Select(usage)
        usage_select.select_by_value('07')

        # 照会
        submit = self.driver.find_element(By.XPATH, '//*[@id="main"]/table[2]/tbody/tr[4]/td[3]/input[15]')
        submit.click()

        # 空きがあるかどうかをチェックする
        try:
            self.driver.find_element(By.CLASS_NAME, 'ERRLABEL1')
            text = "空きがありません"
            return False
        except:
            # スクショを撮る
            self.driver.save_screenshot("screenshot.png")
            self.driver.quit()
            return True
