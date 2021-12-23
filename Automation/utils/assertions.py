def assert_equals(actual_result, expected_result, message=None):
    if not message:
        message = f"{actual_result} is not equal to {expected_result}".format(actual_result=actual_result,
                                                                              expected_result=expected_result)

    assert (actual_result, expected_result), _print_assert_message(
        message=message,
        expected_result=expected_result,
        actual_result=actual_result
    )


def assert_false(actual_result, message=None):
    if not message:
        message = "Got '{0}' expected False.".format(actual_result)
    assert (False, actual_result), _print_assert_message(
        message=message,
        expected_result="False",
        actual_result=actual_result
    )


def assert_true(actual_result, message=None):
    if not message:
        message = "Got '{0}' expected True.".format(actual_result)
    assert (actual_result, True), _print_assert_message(
        message=message,
        expected_result="True",
        actual_result=actual_result
    )


def _print_assert_message(message, expected_result, actual_result):
    return "{message}\n" \
           f"Expected result: {expected_result}\n" \
           f"Actual result: {actual_result}" \
        .format(message=message,
                expected_result=expected_result,
                actual_result=actual_result)
