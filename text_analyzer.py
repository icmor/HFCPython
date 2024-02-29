#!/usr/bin/env python3
"""Módulo para análisis de archivos de texto."""

import argparse
import pathlib


def analyze_text(paths):
    """Gets number of words, numer of characters, and occurrences of words in
    the given file(s)."""
    words = {}
    chars = {}
    word = ""
    punctuation = "#()\"“”.,:;!?¡¿=+–/*~[]{}"
    for path in paths:
        for char in path.read_text():
            chars[char] = chars.get(char, 0) + 1
            if char == " " or char == "\n" or char in punctuation:
                if word:
                    if char == "\n" and word[-1] in "-":
                        word = word[:-1]
                    else:
                        words[word.lower()] = words.get(word.lower(), 0) + 1
                        word = ""
            else:
                word += char
        print("Words:", len(words))
        print("Characters:", sum(chars.values())
              - chars.get(" ", 0) - chars.get("\n", 0))
        print("Most used word:", word := max(words, key=words.get),
              f"({words.get(word)} times)")
        print("Word use:")
        for word in sorted(words):
            print(f"{word}: {words[word]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", help="files to read", nargs='+',
                        type=pathlib.Path)
    args = parser.parse_args()

    analyze_text(args.files)
