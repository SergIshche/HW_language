from selenium.webdriver.common.by import By
import time

def test_find_add_to_basket_btn(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(15)
    assert browser.find_element(By.CLASS_NAME, 'btn-add-to-basket').is_displayed(), \
        '"add to basket" button is not available'