from palindrome import is_palindrome

def test_simple_palindrome():
    assert is_palindrome("racecar") is True

def test_sentence_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_non_palindrome():
    assert is_palindrome("Hello World") is False
