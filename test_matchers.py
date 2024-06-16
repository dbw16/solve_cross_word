import pytest

from matchers import match_known_letters, match_length, match_repeated_letters


@pytest.mark.parametrize(
    "word, guess, expected_result",
    [
        (["a", "1", "1", "l", "e"], ["a", "p", "p", "l", "e"], True),
        (["3", "1", "1", "2", "e"], ["a", "p", "p", "l", "e"], True),
        (["1", "2", "3"], ["a", "p", "p"], True),
        (["c", "a", "t"], ["c", "a", "t"], True),
        (["c", "a", "t"], ["c", "a", "b"], False),
        (["1", "2", "t"], ["c", "a", "b"], False),
    ],
)
def test_filter_known_letters(word, guess, expected_result):
    assert match_known_letters(word, guess) == expected_result


@pytest.mark.parametrize(
    "word, guess, expected_result",
    [
        (["a", "1", "1", "l", "e"], ["a", "p", "p", "l", "e"], True),
        (["3", "1", "1", "2", "e"], ["a", "p", "p", "l", "e"], True),
        (["1", "2", "3"], ["a", "p", "p"], True),
        (["c", "a", "t"], ["c", "a", "t"], True),
        (["c", "a", "t"], ["c", "a", "b"], True),
        (["1", "2", "t"], ["c", "a", "b"], True),
        (["c", "a", "t"], [], False),
        (["c", "a", "t"], ["a", "t"], False),
        (["1"], ["a", "b"], False),
    ],
)
def test_match_length(word, guess, expected_result):
    assert match_length(word, guess) == expected_result


@pytest.mark.parametrize(
    "word, guess, expected_result",
    [
        (["a", "1", "1", "l", "e"], ["a", "p", "p", "l", "e"], True),
        (["3", "1", "1", "2", "e"], ["a", "p", "p", "l", "e"], True),
        (["1", "2", "2"], ["a", "p", "p"], True),
        (["c", "a", "t"], ["c", "a", "t"], True),
        (["c", "a", "t"], ["c", "a", "b"], True),
        (["1", "2", "t"], ["c", "a", "b"], True),
        (["1", "2", "3", "1", "2", "3"], ["a", "b", "c", "a", "b", "c"], True),
        (["1", "1", "1", "1", "2"], ["a", "a", "a", "a", "b"], True),
        (["1", "1", "1", "1", "2"], ["a", "a", "a", "a", "a"], False),
    ],
)
def test_match_repeated_letters(word, guess, expected_result):
    assert match_repeated_letters(word, guess) == expected_result
