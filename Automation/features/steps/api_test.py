from behave import *
from faker import Faker
from configuration.config import TestData
from requestmodule import apis as API
from configuration.contants import Constants as const
from configuration.httpresponses import HTTP_OK
from utils.assertions import assert_equals, assert_true, assert_false

fake = Faker()


@given(u'Create a user through API with random data')
def create_user_random_data(context):
    const.firstname = fake.first_name()
    const.lastname = fake.last_name()
    const.email = fake.email()
    context.url = TestData.BASE_URI
    kwargs_dict = {
        'email': const.email,
        'firstName': const.firstname,
        'lastName': const.lastname,
        'newsletter': "true"
    }
    user_response, status = API.create_api(context.url, **kwargs_dict)
    assert_true(actual_result=user_response,
                message="Create API is returning false")

    assert_equals(actual_result=status,
                  expected_result=HTTP_OK,
                  message="Failed to create user with details {firstname},{lastname}".format(firstname=const.firstname,
                                                                                             lastname=const.lastname))


@then(u'Fetch the details of the user and verify')
def fetch_all_details(context):
    context.url = TestData.BASE_URI
    args = [
        'uuid',
        'email',
        'firstName',
        'lastName'
    ]
    user_details, status = API.fetch_api(context.url, *args)

    # fetching the latest created user's uuid and storing the value
    const.uuid = API.filter_json_data(user_details, 'uuid')

    assert const.firstname, API.filter_json_data(user_details, 'firstName')
    assert const.lastname, API.filter_json_data(user_details, 'lastName')
    assert const.email, API.filter_json_data(user_details, 'email')

    assert_equals(actual_result=status,
                  expected_result=HTTP_OK,
                  message="Failed to fetch the user's details of the user")


@then(u'Delete the user')
def delete_single_user(context):
    context.url = TestData.BASE_URI
    status = API.delete_api(context.url, uuid=const.uuid)

    assert_equals(actual_result=status,
                  expected_result=HTTP_OK,
                  message="Failed to delete the user")


@given(u'Create a user firstname: {firstname}, lastname: {lastname} email:{email} and newsletter as {newsletter}')
def create_user_param_data(context, firstname, lastname, email, newsletter):
    context.url = TestData.BASE_URI

    kwargs_dict = {
        'email': email,
        'firstName': firstname,
        'lastName': lastname,
        'newsletter': newsletter
    }
    user_response, status = API.create_api(context.url, **kwargs_dict)

    assert_true(actual_result=user_response,
                message="Seems user is present with existing email id i.e. {email}".format(email=email))

    assert_equals(actual_result=status,
                  expected_result=HTTP_OK,
                  message="Failed to create user with details {firstname},{lastname}".format(firstname=const.firstname,
                                                                                             lastname=const.lastname))


@then(u'Update the user firstname {firstname}, lastname {lastname}, email {email} and newsletter {newsletter}')
def update_user(context, firstname, lastname, email, newsletter):
    context.url = TestData.BASE_URI
    const.firstname = firstname
    const.lastname = lastname
    const.email = email
    kwargs_dict = {
        "uuid": const.uuid,
        "firstName": const.firstname,
        "lastName": const.lastname,
        "email": const.email,
        "newsletter": newsletter
    }
    update_response, status = API.update_api(context.url, **kwargs_dict)

    assert_true(actual_result=update_response,
                message="Update api is not return true value")

    assert_equals(actual_result=status,
                  expected_result=HTTP_OK,
                  message="Failed to create user with details {firstname},{lastname}".format(firstname=const.firstname,
                                                                                             lastname=const.lastname))


@then(u'Delete all the previous created user')
def delete_all_user(context):
    context.url = TestData.BASE_URI
    args = [
        'uuid'
    ]
    user_details, status = API.fetch_api(context.url, *args)
    assert_equals(actual_result=status,
                  expected_result=HTTP_OK,
                  message="Failed to fetch the user's details of the user")
    context.uuid_list = []
    context.uuid_list = API.fetch_respective_detail(user_details, 'uuid')

    for uuid in range(0, len(context.uuid_list)):
        status = API.delete_api(context.url, uuid=context.uuid_list[uuid])
        assert_equals(actual_result=status,
                      expected_result=HTTP_OK,
                      message="Failed to delete the user")


@given(u'Create a user with different {firstname}, {lastname} and {newsletter} but with same {email}')
def create_user_with_same_email(context, firstname, lastname, newsletter, email):
    context.url = TestData.BASE_URI

    kwargs_dict = {
        'email': email,
        'firstName': firstname,
        'lastName': lastname,
        'newsletter': newsletter
    }
    user_response, status = API.create_api(context.url, **kwargs_dict)

    assert_false(actual_result=user_response,
                 message="User is able to create the data with same email id and email is {email}".format(email=email))

    assert_equals(actual_result=status,
                  expected_result=HTTP_OK,
                  message="Failed to delete the user")


@then(u'Verify only one user should be present if same emails are being used')
def no_same_email_verification(context):
    context.url = TestData.BASE_URI
    args = [
        'uuid',
        'email',
        'firstName',
        'lastName'
    ]
    user_details, status = API.fetch_api(context.url, *args)

    assert_equals(actual_result=len(user_details),
                  expected_result=0,
                  message="More than user have been created i.e. {user_details}".format(user_details=user_details))

    assert_equals(actual_result=status,
                  expected_result=HTTP_OK,
                  message="Failed to delete the user")
