from collections import Counter


def solution(s, t):
    a = sorted(Counter(s).values())
    b = sorted(Counter(t).values())
    return (
        True
        if sorted(Counter(s).values()) == sorted(Counter(t).values())
        else False
    )


def test_solution():
    assert solution("aad", "bbc") is True
    assert solution("kitty", "perry") is True
    assert solution("kitty", "rrpet") is True
    assert solution("foo", "baa") is True
