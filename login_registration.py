# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# btn_1 = driver.find_element_by_id("menu-item-50").click()
# btn_2 = driver.find_element_by_id("reg_email").send_keys("nikitakras@mail.ru")
# btn_3 = driver.find_element_by_id("reg_password")
# btn_3.send_keys("Nikita234730GG")
# btn_4 = driver.find_element_by_css_selector(".u-column2").click()
# btn_5 = driver.find_element_by_name("register").click()

from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(5)
btn = driver.find_element_by_id("menu-item-50").click()
btn_1 = driver.find_element_by_id("username").send_keys("nikitakras@mail.ru")
btn_2 = driver.find_element_by_id("password").send_keys("Nikita234730GG")
btn_3 = driver.find_element_by_name("login").click()
element = driver.find_element_by_css_selector("nav:nth-child(1) li:nth-child(6) a")
element_get_text = element.text
assert element_get_text == "Logout"
