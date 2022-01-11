from behave import *

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from configuration.config import TestData
from pagefactory.HomePage import HomePage
from pagefactory.Users import Users
from faker import Faker
from configuration.contants import Constants as const
from nose.tools import assert_false
from utils.customuitls import user_error_message, home_list_view, home_before_user_creation, user_page_elements, \
    invalid_email_err_msg, page_title

fake = Faker()


@given('Launch the browser')
def launch_browser(context):
    try:
        # This code work in case a user wants to run the ui automation in some standalone server
        context.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                          desired_capabilities=DesiredCapabilities.CHROME
                                          )
        # Below line is when user wants to run the automation in the local browser
        # context.driver = webdriver.Chrome(ChromeDriverManager().install())

        context.driver.maximize_window()
        context.driver.get(TestData.URL)
    except:
        context.driver.close()
        assert_false()


@then(u'Validate the page title')
def validate_page_title(context):
    try:
        context.home = HomePage(context.driver)
        assert context.driver.title, page_title()
    except:
        context.driver.close()
        assert_false(True, msg="Test failed during getting the page's title")


@then('Click on the create user button')
def click_create_user_button(context):
    try:
        context.home = HomePage(context.driver)
        context.home.create_user_click()
    except:
        context.driver.close()
        assert_false("False", msg="User is not able to click on the delete button")


@then('Enter the details of the user')
def enter_user_details(context):
    try:
        context.user = Users(context.driver)

        const.firstname = fake.first_name()
        const.lastname = fake.last_name()
        const.email = fake.email()

        context.user.enter_first_name(const.firstname)
        context.user.enter_last_name(const.lastname)
        context.user.enter_email(const.email)
    except:
        context.driver.close()
        assert_false("False", msg="Test failed in entering the user's details")


@then('Click on the submit button')
def click_submit_button(context):
    try:
        context.user = Users(context.driver)
        context.user.click_submit_button()
    except:
        context.driver.close()
        assert_false("False", msg="Test failed in submitting the user's details")


@given('Delete all the present user')
def delete_all_present_user(context):
    try:
        context.home = HomePage(context.driver)
        context.home.delete_all_user()
    except:
        context.driver.close()
        assert_false("False", msg="Test failed during the deletion of user's data")


@then('Verify the visibility of elements on the user home screen')
def verify_visibility_of_home_elements(context):
    try:
        context.home = HomePage(context.driver)
        assert home_list_view(), context.home.verify_home_view()
    except:
        context.driver.close()
        assert_false(True, msg="Test failed during the verification of visibility of home elements")


@then(u'Verify the visibility of elements on the user home screen before user creation')
def home_screen(context):
    try:
        context.home = HomePage(context.driver)
        assert home_before_user_creation(), context.home.verify_data_before_user_creation()
    except:
        context.driver.close()
        assert_false("False", msg="Test failed during the verification of visibility of home "
                                  "elements before user creation")


@then(u'Click on the delete button')
def delete_button(context):
    try:
        context.home = HomePage(context.driver)
        context.home.delete_user()
    except:
        context.driver.close()
        assert_false("False", msg="Test failed while clicking on delete button")


@then(u'Validate the created user detail on the home screen')
def validate_user_info(context):
    try:
        context.home = HomePage(context.driver)
        assert True, context.home.validate_user_details()
    except:
        context.driver.close()
        assert_false("False", msg="Test failed on validating the user's detail")


@then(u'Verify the validation message on the user creation page')
def user_creation_validation_err_msg(context):
    try:
        context.user = Users(context.driver)
        assert user_error_message(), context.home.validate_user_error_messages()
    except:
        context.driver.close()
        assert_false("False", msg="Test failed on verification of user's details")


@then(u'Verify the visibility of the elements on the user creation screen')
def user_screen_validation(context):
    try:
        context.user = Users(context.driver)
        assert context.user.verify_user_screen(), user_page_elements()
    except:
        context.driver.close()
        assert_false("False", msg="Test failed during the verification of visibility of user screen "
                                  "element")


@then(u'Validate the user info as {firstname}, {lastname} and {email}')
def validate_user_info(context, firstname, lastname, email):
    try:
        context.user = Users(context.driver)
        context.user.enter_first_name(firstname=firstname)
        context.user.enter_last_name(lastname=lastname)
        context.user.enter_email(email=email)
        context.user.click_submit_button()
    except:
        context.driver.close()
        assert_false("False", msg="Test failed during the user details during invalid scenario")


@then(u'Validate the invalid email error')
def invalid_email_err_msg(context):
    try:
        context.user = Users(context.driver)
        assert context.user.invalid_email_error_message(), invalid_email_err_msg()
    except:
        context.driver.close()
        assert_false("False", msg="Test failed during validating the invalid email error message")
