from main import double_number


def test_double():
    """Testing double function"""
    assert double_number(1) == 2
    assert double_number(3) == 6
    assert double_number(5) == 10
    print("Success")


if __name__ == "__main__":
    test_double()
