"""
This project categorizes Canadian federal legislation
"""

from preprocessor import *

US_BILLS_RAW = 'data\\us_bills.csv'

if __name__ == "__main__":
    preproc = Preprocessor(US_BILLS_RAW)
    preproc.do_preprocess()
