import pandas as pd
import numpy as np


class Trainer:
    """
    Uses a bag of words model to train the Naive Gauss algorithm
    """

    training_data = pd.DataFrame()  # type: pd.DataFrame
    bow_dicts = []  # type: list[dict]
    categories = []  # type: list[str]
    num_categories = 0  # type: int

    def __init__(self, training_data, categories):
        self.training_data = training_data
        self.categories = categories
        self.num_categories = len(categories)
        self.bow_dicts = [{} for i in range(self.num_categories)]

    def train(self):
        """
        Trains the model
        """
        td = self.training_data

        for ind, cat in enumerate(self.categories):
            cat_exs = td.loc[td['Major'] == ind+1]
            titles_lst = cat_exs['Title']




