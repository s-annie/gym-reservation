import time
import chromedriver_binary
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://www.net.city.nagoya.jp/sporec/index.html')

place_search = driver.find_element(By.XPATH, '//a[@href="https://www.net.city.nagoya.jp/cgi-bin/sp04001"]')
place_search.click()

# 種目の選択
event = driver.find_element(By.NAME, 'syumoku')
event_select = Select(event)
event_select.select_by_value('024')

# 利用日の選択
month = driver.find_element(By.NAME, 'month')
month_select = Select(month)
month_select.select_by_value('05')

day = driver.find_element(By.NAME, 'day')
day_select = Select(day)
day_select.select_by_value('19')

# 希望条件の選択
# radio_button = driver.find_element(By.XPATH, '//*[@id="main"]/table[2]/tbody/tr[2]/td[4]/input[2]')
# radio_button.click()

# 供用区分の選択
usage = driver.find_element(By.NAME, 'kyoyo1')
usage_select = Select(usage)
usage_select.select_by_value('07')

# 照会
submit = driver.find_element(By.XPATH, '//*[@id="main"]/table[2]/tbody/tr[4]/td[3]/input[15]')
submit.click()

# 空きがあるかどうかをチェックする
try:
    driver.find_element(By.CLASS_NAME, 'ERRLABEL1')
    text = "空きがありません"
except:
    # スクショを撮る
    driver.save_screenshot("screenshot.png")
    driver.quit()
