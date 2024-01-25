
class takenBook():
    person = ''
    date = ''
    book = ''
    backDate = ''
    backed = False

    def __init__(self, book, person, date, backDate, backed):
        self.book = book
        self.person = person
        self.date = date
        self.backDate = backDate
        self.backed = backed