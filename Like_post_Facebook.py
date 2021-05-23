import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# chạy trình duyệt ẩn danh
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(chrome_options=chrome_options)

#độ lớn cửa sổ trình duyệt
browser.maximize_window()

#link dẫn tới trang web
browser.get("https://vi-vn.facebook.com")

# tìm id email và nhập email
email = browser.find_element_by_id('email')
email.send_keys("username@gmail.com")
time.sleep(1)

# tìm id pass và nhập pass
passw = browser.find_element_by_id('pass')
passw.send_keys("password")
time.sleep(1)

# tìm name login và đăng nhập
btnLogin = browser.find_element_by_name('login')
btnLogin.send_keys(Keys.ENTER)
time.sleep(1)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

likes = browser.find_elements_by_xpath(
    "//div[@class='tvfksri0 ozuftl9m']//div[@aria-label='Thích']")
actions = ActionChains(browser)
print(len(likes))
time.sleep(5)

for i in range(0, 5):
    actions.move_to_element(likes[i]).perform()
    browser.execute_script("arguments[0].click();", likes[i])
    print(likes[i])
    time.sleep(1)

time.sleep(3)
browser.close()
