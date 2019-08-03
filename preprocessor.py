
import pandas as pd


class Preprocessor:
    """
    Preprocesses a csv file of classified US bills for training
    """

    data_path = ''  # type: str
    data = pd.DataFrame()  # type: pd.DataFrame

    def __init__(self, data_path):
        self.data_path = data_path

    def do_preprocess(self):
        """
        Does preprocessing
        """
        print('Reading US Bills...')
        self.read_and_filter()
        print ('Done reading.')
        return

    def read_and_filter(self):
        """
        Reads US bills and filters those with a category
        """

        data = pd.read_csv(self.data_path, delimiter=';')
        # data = data.filter(['BillNum', 'Title', 'Major'])
        data.head(5)

        self.data = data


