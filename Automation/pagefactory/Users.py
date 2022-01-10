from pagefactory.BasePage import BasePage
from selenium.webdriver.common.by import By


class Users(BasePage):
    first_name_text_box_id = (By.ID, "mat-input-0")
    last_name_text_box_id = (By.ID, "mat-input-1")
    email_text_box_id = (By.ID, "mat-input-2")
    news_letter_checkbox_id = (By.ID, "mat-checkbox-1-input")
    submit_button_xpath = (By.XPATH, "//button[@type='submit']")
    first_name_error_id = (By.ID, "mat-error-0")
    last_name_error_id = (By.ID, "mat-error-1")
    email_error_id = (By.ID, "mat-error-2")
    valid_email_error_xpath = (By.XPATH, "//mat-error[contains(text(),'Please enter a valid email.')]")
    first_name_formcontrol_name = (By.XPATH, "//mat-label[contains(text(),'First Name')]")
    last_name_formcontrol_name = (By.XPATH, "//mat-label[contains(text(),'Last Name')]")
    email_formcontrol_name = (By.XPATH, "//mat-label[contains(text(),'Email Address')]")
    newsletter_checkox_txt = (By.XPATH, "//span[contains(text(),'Signup for our newsletter.')]")
    create_new_user_txt = (By.XPATH, "//h1[contains(text(),'Create New User')]")

    def __init__(self, driver):
        super().__init__(driver)

    def verify_user_screen(self):
        user_list = [
            self.get_text(self.create_new_user_txt),
            self.get_text(self.first_name_formcontrol_name),
            self.get_text(self.last_name_formcontrol_name),
            self.get_text(self.email_formcontrol_name),
            self.get_text(self.newsletter_checkox_txt),
            self.get_text(self.submit_button_xpath)
        ]
        return user_list

    def enter_first_name(self, firstname):
        self.do_send_keys(self.first_name_text_box_id, firstname)

    def enter_last_name(self, lastname):
        self.do_send_keys(self.last_name_text_box_id, lastname)

    def enter_email(self, email):
        self.do_send_keys(self.email_text_box_id, email)

    def click_submit_button(self):
        self.do_click(self.submit_button_xpath)

    def select_for_news_letter(self):
        self.do_click(self.news_letter_checkbox_id)

    def validate_user_error_messages(self):
        error_list = [
            self.get_text(self.first_name_error_id),
            self.get_text(self.last_name_error_id),
            self.get_text(self.email_error_id)
        ]

        return error_list

    def invalid_email_error_message(self):
        return self.get_text(self.valid_email_error_xpath)
