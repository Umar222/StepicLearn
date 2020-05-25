def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, "expected {}, got {}" \
        .format(expected_result, actual_result)


test_input_text(8, 11)


def test_substring(full_string, substring):
    assert substring not in full_string, "expected '{}' to be substring of '{}'" \
        .format(substring, full_string)


test_substring("test", "uert")
