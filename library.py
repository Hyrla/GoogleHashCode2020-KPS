class Library:
    def __init__(self, id, books, nb_days, nb_scan_by_days, max_score = 0):
        self.id = id
        self.books = books
        self.nb_day = nb_days
        self.nb_scan_by_days = nb_scan_by_days
        self.max_score = max_score
