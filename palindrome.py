def is_palindrome(s: str) -> bool:
    if s is None:
        return False
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

is_palindrome("tes")