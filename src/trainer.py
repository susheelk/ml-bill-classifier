import pandas as pd
import numpy as np
import os
from category import Category
from output_model import OutputModel

OUTPUT_DIR = 'data/output_model/'


class Trainer:
    """
    Uses a bag of words model to train the Naive Gauss algorithm
    """

    training_data = pd.DataFrame()  # type: pd.DataFrame
    # bow_dicts = []  # type: list[dict[str, int]]

    categories = []  # type: list[Category]

    categories_url = ''  # type: # str
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
        self.__construct_bows()
        print 'Vocab size: ' + str(self.vocabulary_size)
        print 'Calculating category denoms...'
        self.__calculate_cat_denoms()

    def __construct_bows(self):
        td = self.training_data
        num_examples = float(td.size)

        for ind, category in enumerate(self.categories):
            cat_exs = td.loc[td['Major'] == ind+1]
            if (cat_exs.size != 0) and (str(category.name) != 'nan'):
                words_arr = np.hstack(np.array(cat_exs['Title'].values))
                category.bow_dict = {}  # prevent unwanted references
                [self.__add_to_bow(ind, word) for word in words_arr]

                # Calculate prior probability of this category
                category.prior_prob = float(cat_exs.size) / num_examples

                print '\t' + category.name + '\t(' + str(ind+1) + '/' + str(len(self.categories)) + ')'
        self.vocabulary_size = len(self.vocabulary)

    def __calculate_cat_denoms(self):
        for category in self.categories:
            if str(category.name) == 'nan':
                continue
            bow_dict = category.bow_dict
            count = sum(bow_dict.values())
            category.word_prob_denom = count + self.vocabulary_size + 1
            print '\t' + category.name

    def write_model_csv(self):
        out_dir = OUTPUT_DIR + 'categories/'
        if not os.path.isdir(out_dir):
            os.mkdir(OUTPUT_DIR)
            os.mkdir(out_dir)

        for num, category in enumerate(self.categories):
            cat_name = category.name
            if str(cat_name) != 'nan':
                df = pd.DataFrame.from_dict(category.bow_dict, orient='index', columns=['Occurrences'])
                df.to_csv(path_or_buf=out_dir + cat_name + '.csv', index=True, index_label='Word')

        denoms = dict([(cat.name, cat.word_prob_denom) for cat in self.categories])
        priors = dict([(cat.name, cat.prior_prob) for cat in self.categories])

        denom_df = pd.DataFrame.from_dict(denoms, orient='index', columns=['Denoms'])
        priors_df = pd.DataFrame.from_dict(priors, orient='index', columns=['Priors'])

        denom_df.to_csv(path_or_buf=OUTPUT_DIR + 'denoms.csv', index=True, index_label='Category')
        priors_df.to_csv(path_or_buf=OUTPUT_DIR + 'priors.csv', index=True, index_label='Category')

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
        self.categories = [Category(name=x) for x in category_names]
        self.num_categories = len(self.categories)
        # self.bow_dicts = [{} for i in range(self.num_categories)]

    def get_output_model(self):
        return OutputModel(self.categories, self.vocabulary_size)
