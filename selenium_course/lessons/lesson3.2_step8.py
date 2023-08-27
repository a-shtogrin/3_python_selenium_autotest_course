def test_input_text(expected_result, actual_result):
    assert actual_result == expected_result, f"expected {expected_result}, got {actual_result}"

def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_substring("1 2 3 4 5", "1")
    test_input_text(125, 125)
    print("All tests passed!")

