"""
This project categorizes Canadian federal legislation
"""

import os
from constants import *
from preprocessor import *
from trainer import *
import pandas as pd
from output_model import OutputModel
from naive_bayes_predictor import NaiveBayesPredictor


def get_cat_bow_file(cat_path):
    df = pd.read_csv(cat_path, delimiter=',')
    return df.set_index('Word')['Occurrences'].to_dict()


def get_denoms():
    df = pd.read_csv(OUTPUT_PATH + 'denoms.csv')
    return df.set_index('Category')['Denoms'].to_dict()


def get_priors():
    df = pd.read_csv(OUTPUT_PATH + 'priors.csv')
    return df.set_index('Category')['Priors'].to_dict()


def read_from_disk():
    """
    Reads the pre-trained output model from file
    :return: the trained OutputModel
    """
    print 'Reading Categories from file.. '

    if not os.path.isdir(OUTPUT_PATH):
        raise Exception('No Output Model Found!')

    denoms = get_denoms()
    priors = get_priors()

    categories_path = OUTPUT_PATH + 'categories/'
    categories = []

    for filename in os.listdir(categories_path):
        if filename.endswith('.csv'):
            bow_dict = None  # prevent unwanted reference leaks
            bow_dict = get_cat_bow_file(categories_path + filename)
            name = filename[:-4]
            categories.append(Category(name=name, word_prob_denom=denoms[name], prior_prob=name, bow_dict=bow_dict))
            print '\t' + name
    return categories


def get_all_examples():
    preproc = Preprocessor(data_path=US_BILLS_RAW,
                           exclude_words=EXCLUDE_WORDS.split(' '),
                           phrase_map=WORD_MAP)
    return preproc.do_preprocess()

def train(training_data):
    """
    Trains the model
    :return: the trained OutputModel
    """
    trainer = Trainer(training_data=training_data, categories_url=CATEGORIES_MAP)
    trainer.train()
    trainer.write_model_csv()
    return trainer.get_output_model()


if __name__ == "__main__":
    output_model = None
    test_data = None

    examples = get_all_examples()
    train_len = int(float(len(examples)) * float(TRAIN_PERCENTAGE) / 100)
    test_data = examples.tail(len(examples) - train_len)

    if TRAIN:
        training_data = examples.head(train_len)
        output_model = train(training_data)
    else:
        output_model = read_from_disk()

    predictor = NaiveBayesPredictor(output_model)


