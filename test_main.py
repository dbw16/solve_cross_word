import pytest

from main import find_matches


@pytest.mark.parametrize(
    "word, expected_result",
    [
        (
            ["a", "p", "p", "l", "e"],
            {
                "apple",
            },
        ),
        (
            ["1", "p", "p", "l", "e"],
            {
                "apple",
            },
        ),
        (["a", "1", "1", "l", "e"], {"apple", "addle", "attle"}),
    ],
)
def test_find_matches(word, expected_result):
    assert find_matches(word) == expected_result
