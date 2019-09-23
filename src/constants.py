US_BILLS_RAW = '/data/us_bills.csv'
CATEGORIES_MAP = 'data/classes.csv'
OUTPUT_PATH = 'data/output_model/'
TRAIN_PERCENTAGE = 2

# American to Canadian translations for preprocessor
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
    'defense': 'defence',
    'federal reserve system': 'bank of canada',
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

EXCLUDE_WORDS = 'a an bill to for that to the is he act of from and in by as other or at as such be act amend'
TRAIN = True  # Setting to true will retrain
