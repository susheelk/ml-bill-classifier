import numpy as np


class Category:
    name = ''  # type: str
    cat_id = -1  # type: int
    bow_dict = {}  # type: dict[str, int]
    prior_prob = 0  # type: int
    word_prob_denom = 1  # type: int

    # Calculated values
    total_word_count = 0

    def __init__(self, name, cat_id, prior_prob=0, word_prob_denom=1, bow_dict={}):
        self.name = name
        self.prior_prob = prior_prob
        self.word_prob_denom = word_prob_denom
        self.bow_dict = bow_dict
        self.cat_id = cat_id

    def __calc_word_probability(self, word):
        """
        Calculates the probability of one word for this category
        :param word:
        :return: the probabiliy
        """
        numer = float(self.bow_dict[word] if word in self.bow_dict else 0 + 1)
        return numer / float(self.word_prob_denom)

    def calc_example_probability(self, words_lst):
        word_probs = np.fromiter((self.__calc_word_probability(word) for word in words_lst), float)
        example_prob = np.sum(word_probs) * self.prior_prob
        return example_prob
