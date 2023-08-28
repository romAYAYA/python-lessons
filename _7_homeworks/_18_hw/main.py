def is_anagram(phrase: str, check_phrase: str) -> bool:
    phrase = phrase.replace(" ", "").lower()
    check_phrase = check_phrase.replace(" ", "").lower()

    return sorted(phrase) == sorted(check_phrase)


if __name__ == '__main__':
    print(is_anagram(phrase='рано', check_phrase='нора'))
