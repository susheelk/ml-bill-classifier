import pandas as pd
import numpy as np


class Trainer:
    """
    Uses a bag of words model to train the Naive Gauss algorithm
    """

    training_data = pd.DataFrame()  # type: pd.DataFrame
    bow_dicts = []  # type: list[dict]
    categories = []  # type: list[str]
    categories_url = ''  # type: str
    num_categories = 0  # type: int

    def __init__(self, training_data, categories_url):
        self.training_data = training_data
        self.categories_url = categories_url
        self.__read_categories()

    def train(self):
        """
        Trains the model
        """
        td = self.training_data

        for ind, cat in enumerate(self.categories):
            cat_exs = td.loc[td['Major'] == ind+1]
            words_arr = np.array(cat_exs['Title'].values.flatten())
            self.__add_to_bow(ind, words_arr)

    def __add_to_bow(self, dict_ind, word):
        self.bow_dicts[dict_ind][word] += 1

    def __read_categories(self):
        df = pd.read_csv(self.categories_url, delimiter=',')
        self.categories = df['Category']
        self.num_categories = len(self.categories)
        self.bow_dicts = [{} for i in range(self.num_categories)]






