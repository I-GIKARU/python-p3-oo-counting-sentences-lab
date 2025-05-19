#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # uses the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        if not self._value:
            return 0
        # Split using regex on punctuation that ends a sentence: ., !, or ?
        # Handles multiple punctuation marks like "!!" or "??"
        sentences = re.split(r'[.!?]+', self._value)
        # Filter out empty strings or whitespace-only fragments
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
