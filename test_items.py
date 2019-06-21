import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_user_should_see_add_to_basket_button(browser, link):
    browser.get(link)
    time.sleep(30)
    browser.find_element_by_css_selector("button.btn-add-to-basket")
