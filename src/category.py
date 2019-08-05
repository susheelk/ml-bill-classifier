class Category:
    name = ''  # type: str
    bow_dict = {}  # type: dict[str, int]
    prior_prob = 0  # type: int
    word_prob_denom = 1  # type: int

    def __init__(self, name):
        self.name = name
        self.bow_dict = {}