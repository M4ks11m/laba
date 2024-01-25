class Book():
    
    name = ''
    authors = ''
    code = ''
    date = ''
    place = ''
    pubHouse = ''
    sumQuan = 0 
    realQuan = 0

    def __init__(self, name, authors, code, date, place, pubHouse, sumQuan, realQuan):
        self.name = name
        self.authors = authors
        self.code = code
        self.date = date
        self.place = place
        self.pubHouse = pubHouse
        self.sumQuan = sumQuan
        self.realQuan = realQuan
        
