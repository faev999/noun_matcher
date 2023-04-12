#!/usr/bin/env python3
"""
This script takes the most common nouns of two languages, which are stored in 2 files that also contain the
corresponding english translation for each noun, and using said english translation finds which nouns are common on
both languages. There is an example on how to use it for german and spanish nouns and in the example 
nouns which are masculine or femenine in both languages are grouped together
"""
from typing import Dict, List, Tuple


def classify_word_by_gender(
    article: str, word: str, gender_dict: Dict[str, List[str]]
) -> Dict[str, List[str]]:
    """Classify the English translation of a word by its gender."""
    gender = determine_gender(article)
    gender_dict[gender].append(word)
    return gender_dict


def determine_gender(article: str) -> str:
    """Determine the gender of a word based on the article."""
    article = article.lower()
    if article in ["la", "las", "die"]:
        return "fem"
    elif article in ["el", "los", "der"]:
        return "masc"
    else:
        return "neut"


def clasiffy_words_by_lang_and_gen(
    file_nouns_english_target_lang: str, target_lang: str
) -> Tuple[List[str], Dict[str, str], Dict[str, List[str]]]:
    """
    Read a file containing nouns in the target language with their English translations, and
    create a dictionary of English nouns with gender as the key.
    """
    english_for_language_gend = (
        {"fem": [], "masc": []}
        if target_lang == "spanish"
        else {"fem": [], "masc": [], "neut": []}
    )
    try:
        with open(file_nouns_english_target_lang, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Error: {file_nouns_english_target_lang} not found. Please provide a valid file path."
        )
    list_english_translations = []
    english_and_target_lang_word_dict = {}

    for line in lines:
        translation, word = line.strip().split("–")
        english_translation = translation.split(".")[1].strip()
        word_in_target_lang = word.strip()
        article = word_in_target_lang.split(" ")[0]
        list_english_translations.append(english_translation)
        english_and_target_lang_word_dict[english_translation] = word_in_target_lang
        classify_word_by_gender(article, english_translation, english_for_language_gend)

    return (
        list_english_translations,
        english_and_target_lang_word_dict,
        english_for_language_gend,
    )


def write_common_words_to_file(
    lang_dict1: Dict[str, str],
    lang_dict2: Dict[str, str],
    common_english_words: List[str],
    file_common_nouns_both_lang: str,
) -> None:
    """Write common words between 2 dictionaries to a file"""
    with open(file_common_nouns_both_lang, "w") as file:
        for word in common_english_words:
            file.write(f"{word}: [{lang_dict1[word]}, {lang_dict2[word]}]\n")


def find_common_english_words_within_2_sets(
    words_lang1: List[str], words_lang2: List[str]
) -> List[str]:
    """find common elements between 2 arrays"""
    return sorted(list(set(words_lang1).intersection(set(words_lang2))))


def main():
    try:
        (
            english_for_spanish_words,
            english_for_spanish_dict,
            english_for_spanish_words_gend,
        ) = clasiffy_words_by_lang_and_gen("spanish_english.txt", "spanish")
        (
            english_for_german_words,
            english_for_german_dict,
            english_for_german_words_gend,
        ) = clasiffy_words_by_lang_and_gen("german_english.txt", "german")
    except FileNotFoundError as e:
        print(e)
        return

    common_english_words = find_common_english_words_within_2_sets(
        english_for_spanish_words, english_for_german_words
    )
    common_english_words_masc = find_common_english_words_within_2_sets(
        english_for_spanish_words_gend["masc"], english_for_german_words_gend["masc"]
    )
    common_english_words_fem = find_common_english_words_within_2_sets(
        english_for_spanish_words_gend["fem"], english_for_german_words_gend["fem"]
    )

    write_common_words_to_file(
        english_for_german_dict,
        english_for_spanish_dict,
        common_english_words,
        "common_pop_german_spanish_words.txt",
    )
    write_common_words_to_file(
        english_for_german_dict,
        english_for_spanish_dict,
        common_english_words_masc,
        "common_pop_german_spanish_masc.txt",
    )
    write_common_words_to_file(
        english_for_german_dict,
        english_for_spanish_dict,
        common_english_words_fem,
        "common_pop_german_spanish_fem.txt",
    )


if __name__ == "__main__":
    main()
