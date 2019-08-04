import pandas as pd
import numpy as np
import os
from category import Category


class Trainer:
    """
    Uses a bag of words model to train the Naive Gauss algorithm
    """

    training_data = pd.DataFrame()  # type: pd.DataFrame
    #bow_dicts = []  # type: list[dict[str, int]]

    categories = []  # type: list[Category]

    categories_url = ''  # type: str
    num_categories = 0  # type: int
    vocabulary = set()  # type: set[str]
    vocabulary_size = 0  # type: int

    def __init__(self, training_data, categories_url):
        print 'Starting Training...'
        self.training_data = training_data
        print 'Size of Training data: ' + str(training_data.size)
        self.categories_url = categories_url
        self.__read_categories()

    def train(self):
        """
        Trains the model
        """
        print 'Constructing models...'
        self.construct_bows()

    def construct_bows(self):
        td = self.training_data

        for ind, category in enumerate(self.categories):
            cat_exs = td.loc[td['Major'] == ind+1]
            if (cat_exs.size != 0) and (str(category.name) != 'nan'):
                words_arr = np.hstack(np.array(cat_exs['Title'].values))
                [self.__add_to_bow(ind, word) for word in words_arr]
                print '\t' + category.name

    def write_bows_csv(self):
        if not os.path.isdir('data/out/'):
            os.mkdir('data/out')

        for num, category in enumerate(self.categories):

            cat_name = category.name
            if str(cat_name) != 'nan':
                df = pd.DataFrame.from_dict(category.bow_dict, orient='index', columns=['Occurrences'])
                df.to_csv(path_or_buf='data/out/' + cat_name + '.csv', index=True, index_label='Word')

    def __add_to_bow(self, cat_ind, word):
        if word in self.categories[cat_ind].bow_dict.keys():
            self.categories[cat_ind].bow_dict[word] += 1
        else:
            self.categories[cat_ind].bow_dict[word] = 1
        self.vocabulary.add(word)

    def __read_categories(self):
        print 'Reading Categories...'
        df = pd.read_csv(self.categories_url, delimiter=',')

        category_names = list(df['Category'])
        self.categories = [Category(x) for x in category_names]
        self.num_categories = len(self.categories)
        # self.bow_dicts = [{} for i in range(self.num_categories)]
