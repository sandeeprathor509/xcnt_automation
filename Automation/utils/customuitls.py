def page_title():
    return "Cashcog Expense Report"


def user_error_message():
    error = [
        "First name is required.",
        "Last name is required.",
        "Email is required."
    ]
    return error


def home_list_view():
    element_visibility = [
        True,
        True,
        "User Overview",
        "First Name",
        "Last Name",
        "Email",
        "Newsletter",
        "Created At",
        "Modified At",
        "Delete"
    ]
    return element_visibility


def home_before_user_creation():
    element_visible = [
        True,
        True,
        "User Overview",
        "No data received!"
    ]

    return element_visible


def user_page_elements():
    element_visible = [
        "Create New User",
        "First Name",
        "Last Name",
        "Email Address",
        "Signup for our newsletter.",
        True
    ]
    return element_visible


def invalid_email_err_msg():
    return "Please enter a valid email."

