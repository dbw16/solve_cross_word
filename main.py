from pathlib import Path

from matchers import match_known_letters, match_length, match_repeated_letters


def load_all_known_words(path: Path) -> tuple[tuple[str, ...], ...]:
    return tuple({tuple((c.lower() for c in word)) for word in path.read_text().splitlines() if word.isalpha()})


def find_matches(word: tuple[str, ...]) -> set[str]:
    matchers = [
        match_length,
        match_repeated_letters,
        match_known_letters,
    ]  # the order these match rules get applied is important

    possible_words = load_all_known_words(Path("words.txt"))

    for matcher in matchers:
        possible_words = tuple(filter(lambda guess: matcher(word, guess), possible_words))

    return {"".join(word) for word in possible_words}


def main() -> None:
    print(find_matches(("1", "p", "1", "2", "3")))


if __name__ == "__main__":
    main()
