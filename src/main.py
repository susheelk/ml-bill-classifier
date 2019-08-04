"""
This project categorizes Canadian federal legislation
"""

from preprocessor import *

US_BILLS_RAW = '../data/us_bills.csv'
WORD_MAP = {
    'congressional': 'parliamentary',
    'congress': 'parliament',
    'department of state': 'department of global affairs',
    'department of homeland security': 'department of public safety',
    'secretary of': 'minister of',
    'of state': 'of global affairs',
    'of homeland security': 'of public safety',
    'state': 'province',
    'presidential': 'prime ministerial',
    'president': 'prime minister',
    'gubernatorial': 'premier\'s',
    'governor': 'premier',
    'social security': 'social insurance',
    'united states': 'canada',
    'american': 'canadian',
    'federal bureau of investigation': 'royal canadian mounted police',
    'central intelligence agency': 'canadian security intelligence service',
    'internal revenue service': 'canada revenue agency',
    'internal revenue': 'canada revenue',
    'california': 'province of british columbia',
    'state of new york': 'province of ontario',
    'new york city': 'city of toronto',
    'state of texas': 'province of alberta',
    'state of alaska': 'yukon territory',
    'color': 'colour'
}
EXCLUDE_WORDS = 'a an bill to for that to the is he act'

# American to Canadian translations


if __name__ == "__main__":
    preproc = Preprocessor(data_path=US_BILLS_RAW,
                           exclude_words=EXCLUDE_WORDS.split(' '),
                           phrase_map=WORD_MAP)
    training_data = preproc.do_preprocess()

