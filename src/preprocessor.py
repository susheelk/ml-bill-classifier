import string

import pandas as pd
import numpy as np

class Preprocessor:
    """
    Preprocesses a csv file of classified US bills for training
    """

    data_path = ''  # type: str
    data = pd.DataFrame()  # type: pd.DataFrame
    exclude_words = []  # type: list[str]
    phrase_map = {}  # type: dict[str, str]

    def __init__(self, data_path, exclude_words=[], phrase_map = {}):
        self.data_path = data_path
        self.exclude_words = exclude_words
        self.phrase_map = phrase_map

    def do_preprocess(self):
        """
        Does preprocessing
        """
        print('Reading US Bills...')
        self.__read_and_filter()
        print('Formatting...')
        self.__format()
        print('Done Preprocessing')
        return self.data

    def __read_and_filter(self):
        """
        Reads US bills and filters those with a category
        """

        data = pd.read_csv('data/us_bills.csv', delimiter=';')
        data = data.filter(['Title', 'Major'])
        # data = data.drop(x for x in data.Major if x == 'nan')
        data = data.mask(data.Major == 'NaN').dropna()
        self.data = data

    def __format(self):
        data = self.data

        # Will throw FutureWarning
        data['Title'] = data['Title'].map(self.__format_title)

        print data.head(5)

    def __format_title(self, title):
        title = title.lower()
        for key, val in self.phrase_map.items():
            title = title.translate(None, string.punctuation)
            title = title.replace(key, val)

        title = title.split(' ')
        return np.array(filter(lambda t: t.lower() not in self.exclude_words, title))
