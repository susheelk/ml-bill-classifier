import numpy as np
import pandas as pd
import os
from category import Category
from output_model import OutputModel


class NaiveBayesPredictor:
    output_model = None  # type: OutputModel

    def __init__(self, output_model):
        self.output_model = output_model



    # @staticmethod
    # def get_word_category_prediction(word, category, vocab_size):
    #     return

    @staticmethod
    def get_category_prediction(string, category, vocab_size):
        return category.calc_example_probability(string.split(' '))
