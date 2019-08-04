import pandas as pd
import numpy as np

class Trainer:
    """
    Uses a bag of words model to train the Naive Gauss algorithm
    """

    training_data = pd.DataFrame() # type: pd.DataFrame
    bow_dicts = [] # type: list[dict]
    num_categories = 0 # type: int

    def __init__(self, training_data, num_categories):
        self.training_data = training_data

    # def train(self):

