"""
Container class representing state post training
"""


class OutputModel:
    categories = []  # type: list[Category]
    vocabulary_size = 0  # type: int

    def __init__(self, categories, vocabulary_size):
        self.categories = categories
        self.vocabulary_size = vocabulary_size


