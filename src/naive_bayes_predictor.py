import numpy as np
import pandas as pd
import os
from category import Category
from output_model import OutputModel


class NaiveBayesPredictor:
    output_model = None  # type: OutputModel

    def __init__(self, output_model):
        self.output_model = output_model

    def predict_category(self, word_list):
        cat_predictions = [0 for i in range(len(self.output_model.categories))]
        for category in self.output_model.categories:
            cat_predictions[category.cat_id] = category.calc_example_probability(word_list)

        cat_predictions[19] /= 2

        cats = dict(zip([cat.name for cat in self.output_model.categories], cat_predictions))
        print cats

        return self.output_model.categories[cat_predictions.index(max(cat_predictions))]

    # @staticmethod
    # def get_word_category_prediction(word, category, vocab_size):
    #     return

    # def get_category_prediction(word_list, category, vocab_size):
    #     return category.calc_example_probability(word_list)
