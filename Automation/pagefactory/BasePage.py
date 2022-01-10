from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def element_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.is_enabled()

    def get_title(self):
        return self.driver.titile

    def element_displayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except:
            return False

    def get_count(self):
        try:
            element = self.driver.find_element_by_xpath("//tr[@class='mat-row cdk-row']")
            return len(element)
        except:
            return False
