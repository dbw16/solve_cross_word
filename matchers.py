def match_length(word: tuple[str, ...], guess: tuple[str, ...]) -> bool:
    return len(word) == len(guess)


def match_known_letters(word: tuple[str, ...], guess: tuple[str, ...]) -> bool:
    return all(w == g or not w.isalpha() for w, g in zip(word, guess))


def match_repeated_letters(word: tuple[str, ...], guess: tuple[str, ...]) -> bool:
    number_to_letter: dict[str, str] = {}
    mapped_letters: set[str] = set()
    for w, g in zip(word, guess):
        if w.isdigit():
            if w in number_to_letter:
                if number_to_letter[w] != g:
                    return False
            else:
                if g in mapped_letters:
                    return False
                mapped_letters.add(g)
                number_to_letter[w] = g
    return True
