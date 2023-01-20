# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# btn = driver.find_element_by_id("menu-item-50").click()
# btn_1 = driver.find_element_by_id("username").send_keys("nikitakras@mail.ru")
# btn_2 = driver.find_element_by_id("password").send_keys("Nikita234730GG")
# btn_3 = driver.find_element_by_name("login").click()
# btn_4 = driver.find_element_by_id("menu-item-40").click()
# btn_5 = driver.find_element_by_css_selector("[title = 'Mastering HTML5 Forms']").click()
# element = driver.find_element_by_css_selector("[itemprop = 'name']")
# element_get_text = element.text
# assert element_get_text == "HTML5 Forms"

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# btn = driver.find_element_by_id("menu-item-50").click()
# btn_1 = driver.find_element_by_id("username").send_keys("nikitakras@mail.ru")
# btn_2 = driver.find_element_by_id("password").send_keys("Nikita234730GG")
# btn_3 = driver.find_element_by_name("login").click()
# btn_4 = driver.find_element_by_id("menu-item-40").click()
# btn_5 = driver.find_element_by_css_selector(".cat-item.cat-item-19 a").click()
# element = driver.find_elements_by_css_selector("ul.masonry-done li")
# assert len(element) == 3

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# btn = driver.find_element_by_id("menu-item-50").click()
# btn_1 = driver.find_element_by_id("username").send_keys("nikitakras@mail.ru")
# btn_2 = driver.find_element_by_id("password").send_keys("Nikita234730GG")
# btn_3 = driver.find_element_by_name("login").click()
# btn_4 = driver.find_element_by_id("menu-item-40").click()
# element = driver.find_element_by_css_selector(".orderby")
# element_check = element.get_attribute("value")
# element_check_text = print(element_check)
# assert element_check == 'menu_order'
# Select(element).select_by_value("price-desc")
# element = driver.find_element_by_css_selector(".orderby")
# element_check = element.get_attribute("value")
# element_check_text2 = print(element_check)
# assert element_check == 'price-desc'

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# btn = driver.find_element_by_id("menu-item-50").click()
# btn_1 = driver.find_element_by_id("username").send_keys("nikitakras@mail.ru")
# btn_2 = driver.find_element_by_id("password").send_keys("Nikita234730GG")
# btn_3 = driver.find_element_by_name("login").click()
# btn_4 = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 600);")
# btn_5 = driver.find_element_by_css_selector("[title = 'Android Quick Start Guide']").click()
# price1 = driver.find_element_by_css_selector(".price > del > span")
# price1_text = price1.text
# price2 = driver.find_element_by_css_selector(".price > ins > span")
# price2_text = price2.text
# assert price1_text == "₹600.00"
# assert price2_text == "₹450.00"
# book = wait.until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book.click()
# book_close = wait.until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# book_close.click()

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# btn_1 = driver.find_element_by_id("menu-item-40").click()
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 900);")
# btn_2 = driver.find_element_by_css_selector("[data-product_id = '182']").click()
# time.sleep(2)
# element1 = driver.find_element_by_css_selector(".cartcontents")
# element1_text = element1.text
# print(element1_text)
# assert element1_text == "1 Item"
# element2 = driver.find_element_by_css_selector(".amount:nth-child(3)")
# element2_text = element2.text
# print(element2_text)
# assert element2_text == "₹180.00"
# element1.click()
# element3 = wait.until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .amount"), "180.00"))
# element4 = wait.until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .amount"), "183.60"))

# from selenium import webdriver
# import time
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# btn_1 = driver.find_element_by_id("menu-item-40").click()
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 900);")
# btn_2 = driver.find_element_by_css_selector("[data-product_id = '182']").click()
# time.sleep(2)
# btn_3 = driver.find_element_by_css_selector("[data-product_id = '165']").click()
# time.sleep(2)
# btn_4 = driver.find_element_by_css_selector(".cartcontents").click()
# element1 = driver.find_element_by_css_selector("tr:nth-child(1) .remove").click()
# element2 = driver.find_element_by_css_selector(".woocommerce-message a").click()
# element3 = driver.find_element_by_css_selector("tr:nth-child(2) .input-text")
# element3.clear()
# element3.send_keys("3")
# element4 = driver.find_element_by_name("update_cart").click()
# element3_value = element3.get_attribute("value")
# assert element3_value == "3"
# time.sleep(2)
# element5 = driver.find_element_by_name("apply_coupon").click()
# element6 = driver.find_element_by_css_selector(".woocommerce-error li")
# element6_get_text = element6.text
# assert "Please enter a coupon code." in element6_get_text

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 10)
# btn_1 = driver.find_element_by_id("menu-item-40").click()
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 900);")
# btn_2 = driver.find_element_by_css_selector("[data-product_id = '182']").click()
# time.sleep(2)
# btn_3 = driver.find_element_by_css_selector(".cartcontents").click()
# btn_4 = wait.until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
# btn_4.click()
# btn_5 = wait.until(
#     EC.element_to_be_clickable((By.ID, "billing_first_name")))
# btn_5.send_keys("nikita")
# btn_6 = driver.find_element(By.ID, "billing_last_name").send_keys("krasn")
# btn_7 = driver.find_element(By.ID, "billing_email").send_keys("krasn@mail.ru")
# btn_8 = driver.find_element(By.ID, "billing_phone").send_keys("88888888")
# driver.execute_script("window.scrollBy(0, 500);")
# btn_9 = driver.find_element(By.ID, "select2-chosen-1").click()
# btn_10 = driver.find_element(By.ID, "s2id_autogen1_search").send_keys("Honduras")
# btn_11 = driver.find_element(By.ID, "select2-results-1").click()
# btn_12 = driver.find_element(By.ID, "billing_address_1").send_keys("Honduras2")
# btn_13 = driver.find_element(By.ID, "billing_city").send_keys("Honduras223124")
# btn_14 = driver.find_element(By.ID, "billing_state").send_keys("Hondurasus")
# btn_15 = driver.find_element(By.ID, "billing_postcode").send_keys("5346436")
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(2)
# btn_16 = driver.find_element(By.ID, "payment_method_cheque").click()
# btn_17 = driver.find_element(By.ID, "place_order").click()
# element1 = wait.until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received"))
# element2 = wait.until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3) td"), "Check Payments"))



