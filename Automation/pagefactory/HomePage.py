from selenium.webdriver.common.by import By

from pagefactory.BasePage import BasePage


class HomePage(BasePage):
    create_user_btn = (By.XPATH, "//span[contains(text(),'Create User')]")
    delete_user_btn = (By.XPATH, "//mat-icon[contains(text(),'delete_outline')]")
    first_name_text_xpath = (By.XPATH, "(//tr[@class='mat-row cdk-row']/td)[1]")
    last_name_text_xpath = (By.XPATH, "(//tr[@class='mat-row cdk-row']/td)[2]")
    email_text_xpath = (By.XPATH, "(//tr[@class='mat-row cdk-row']/td)[3]")
    logo = (By.XPATH, "//img[@src='/assets/images/xcnt-logo-white.png']")
    user_overview = (By.XPATH, "//h1[contains(text(),'User Overview')]")
    first_name_table = (By.XPATH, "//th[contains(text(),'First Name')]")
    last_name_table = (By.XPATH, "//th[contains(text(),'Last Name')]")
    email_table = (By.XPATH, "//th[contains(text(),'Email')]")
    newsletter_table = (By.XPATH, "//th[contains(text(),'Newsletter')]")
    created_table = (By.XPATH, "//th[contains(text(),'Created At')]")
    modified_table = (By.XPATH, "//th[contains(text(),'Modified At')]")
    delete_table = (By.XPATH, "//th[contains(text(),'Delete')]")
    no_data_text = (By.XPATH, "//p[contains(text(),'No data received!')]")

    def verify_home_view(self):
        home_list = [
            self.element_displayed(self.logo),
            self.element_displayed(self.create_user_btn),
            self.get_text(self.user_overview),
            self.get_text(self.first_name_table),
            self.get_text(self.last_name_table),
            self.get_text(self.email_table),
            self.get_text(self.newsletter_table),
            self.get_text(self.created_table),
            self.get_text(self.modified_table),
            self.get_text(self.delete_table)
        ]

        return home_list

    def verify_data_before_user_creation(self):
        if self.element_displayed(self.no_data_text):
            before_user = [
                self.element_displayed(self.logo),
                self.element_displayed(self.create_user_btn),
                self.get_text(self.user_overview),
                self.get_text(self.no_data_text)
            ]

        else:
            while self.do_click(self.delete_user_btn):
                self.do_click(self.delete_user_btn)
            before_user = [
                self.element_displayed(self.logo),
                self.element_displayed(self.create_user_btn),
                self.get_text(self.user_overview),
                self.get_text(self.no_data_text)
            ]
        return before_user

    def create_user_click(self):
        self.do_click(self.create_user_btn)

    def delete_user(self):
        self.do_click(self.delete_user_btn)

    def validation_error_msg_of_user(self):
        verification = [
            self.get_text(self.first_name_text_xpath),
            self.get_text(self.last_name_text_xpath),
            self.get_text(self.email_text_xpath)
        ]

        return verification

    def validate_user_details(self, firstname, lastname, email):
        first_name = (By.XPATH, "//td[contains(text(),'" + firstname + "')]")
        last_name = (By.XPATH, "//td[contains(text(),'" + lastname + "')]")
        email = (By.XPATH, "//td[contains(text(),'" + email + "')]")
        user_details = [
            self.element_displayed(first_name),
            self.element_displayed(last_name),
            self.element_displayed(email)
        ]

        return user_details

    def delete_all_user(self):
        count = self.get_count()
        for i in range(0, count):
            self.delete_user()
            count -= 1
